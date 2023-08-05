import json
import logging
import os

from newrelic.api.log import NewRelicContextFormatter

from event_consumers.src.logging.new_relic_logger import send_newrelic_log

LOG_FILE_PATH = '/var/www-api/.log/consumer_app.log'
LOG_DIR_PATH = '/var/www-api/.log'
LOG_FORMATTER = '%(levelname)s - %(asctime)s - %(name)s - %(message)s'


def is_valid_path(path: str):
    if os.path.exists(path) or os.access(os.path.dirname(path), os.W_OK):
        return True
    return False


def get_logger(name=None):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    std_out_handler = StdOutHandler()
    std_out_handler.setLevel(logging.INFO)
    logger.addHandler(std_out_handler)

    if not os.environ.get("DISABLE_NEWRELIC_API_LOGGING", False):
        # Instantiate a new log handler
        newrelic_handler = NewRelicAPILogHandler(level=logging.WARN)

        # Get the root logger and add the handler to it
        logger.addHandler(newrelic_handler)

    return logger


class StdOutHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        super(StdOutHandler, self).__init__()

    def format(self, record):
        self.formatter = logging.Formatter(LOG_FORMATTER)
        return super(StdOutHandler, self).format(record)


class FileOutHandler(logging.FileHandler):
    def __init__(self):
        super(FileOutHandler, self).__init__(filename=LOG_FILE_PATH)

    def format(self, record):
        self.formatter = logging.Formatter(LOG_FORMATTER)
        return super(FileOutHandler, self).format(record)


class NewRelicAPILogHandler(logging.Handler):
    """
    A class which sends records to a New Relic via its API.
    """

    def __init__(
            self, level=logging.INFO
    ):
        """
        Initialize the instance with the region and license_key
        """
        logging.Handler.__init__(self, level=level)
        self.formatter = NewRelicContextFormatter()

    def emit(self, record):
        """
        Emit a record.
        Send the record to the New Relic API
        """
        try:
            import urllib.parse

            logging.info(f"{record.getMessage()}")
            data_formatted_dict = json.loads(self.format(record))
            send_newrelic_log(message=data_formatted_dict)

        except Exception:
            self.handleError(record)

    def format(self, record):
        return super(NewRelicAPILogHandler, self).format(record)
