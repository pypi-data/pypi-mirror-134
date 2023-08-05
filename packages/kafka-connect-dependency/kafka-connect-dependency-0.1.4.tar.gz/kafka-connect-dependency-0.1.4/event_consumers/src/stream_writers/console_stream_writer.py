from typing import List

from event_consumers.src.logging import logging_util
from event_consumers.src.model.worker_dto import SinkRecordDTO
from event_consumers.src.stream_writers.stream_writer import StreamWriter

logger = logging_util.get_logger(__name__)


class ConsoleStreamWriter(StreamWriter):

    def __init__(self, config: dict):
        super().__init__(config)

    def write(self, streams: List[SinkRecordDTO]) -> None:
        """
        Writes processed records read from kafka to Elastic search
        :param streams: List of SinkRecordDTO - transformed data to be written to ES
        :return: None
        """
        for sink_record_dto in streams:
            logger.info(f' Key: {sink_record_dto.key} - value: {sink_record_dto.message}')

    def close(self) -> None:
        pass
