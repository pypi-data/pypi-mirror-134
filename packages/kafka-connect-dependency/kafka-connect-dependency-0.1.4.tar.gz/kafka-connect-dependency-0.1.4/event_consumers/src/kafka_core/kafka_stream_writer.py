import json
import os
from typing import TypeVar, Generic, List

from event_consumers.src import BOOTSTRAP_SERVERS_DLQ, SECURITY_PROTOCOL, SASL_MECHANISM
from event_consumers.src.exceptions.usi_exceptions import BadConsumerConfigException
from event_consumers.src.kafka_core.ser_des_util import get_ser_des
from event_consumers.src.stream_writers.stream_writer import StreamWriter
from event_consumers.src.logging import logging_util
from event_consumers.src.utility.common_util import CLIENT_ID
from kafka import KafkaProducer

logger = logging_util.get_logger(__name__)

T = TypeVar('T')


class KafkaStreamWriter(Generic[T], StreamWriter):

    def __init__(self, config: dict):
        self.config = config
        self.kafka_producer = self.__create_kafka_producer()
        if not config.get('topic_name'):
            raise BadConsumerConfigException('missing producer topic name.')
        self.topic = config.get('topic_name')

    def write(self, streams: List[T]) -> None:
        """
        writes message of type T to a kafka topic
        :param streams: list of messages
        :return: None
        """
        for event in streams:
            key = None
            if hasattr(event, 'key'):
                key = event.key

            self.kafka_producer.send(topic=self.topic, key=key, value=json.dumps(event.__dict__))

    def close(self) -> None:
        """
        closes the writer kafka producer object
        :return: None
        """
        if self.kafka_producer:
            self.kafka_producer.close()

    def __create_kafka_producer(self) -> KafkaProducer:
        return KafkaProducer(bootstrap_servers=os.environ.get("BOOTSTRAP_SERVERS_DLQ"),
                             key_serializer=get_ser_des(self.config.get(
                                 'key_serializer', 'STRING_SER')),
                             value_serializer=get_ser_des(self.config.get(
                                 'value_serializer', 'STRING_SER')),
                             acks=self.config.get('acks', 'all'),
                             compression_type=self.config.get('compression_type',
                                                              'gzip'),
                             security_protocol=SECURITY_PROTOCOL,
                             sasl_mechanism=SASL_MECHANISM,
                             retries=self.config.get('retries', 1),
                             linger_ms=self.config.get('linger_ms', 10),
                             client_id=CLIENT_ID)
