import traceback
from typing import List

import boto3
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

from event_consumers.src import ENV, ENV_DEV, ES_HOST
from event_consumers.src.exceptions.usi_exceptions import GenericException
from event_consumers.src.logging import logging_util
from event_consumers.src.model.worker_dto import SinkRecordDTO
from event_consumers.src.stream_writers.stream_writer import StreamWriter

logger = logging_util.get_logger(__name__)


class ESStreamWriter(StreamWriter):

    def __init__(self, config: dict):
        super().__init__(config)

        self.es_host = config.get('es_host', ES_HOST)
        self.env = ENV
        self.aws_region = config.get('es_aws_region', 'us-east-1')
        self.request_timeout = config.get('es_request_timeout', '1m')
        self.client = self._get_es_client()

    def _get_es_client(self):
        awsauth = None
        if self.env != ENV_DEV:
            credentials = boto3.Session().get_credentials()
            awsauth = AWS4Auth(
                credentials.access_key,
                credentials.secret_key,
                self.aws_region,
                'es',
                session_token=credentials.token
            )

        return Elasticsearch(
            hosts=[self.es_host],
            http_auth=awsauth,
            use_ssl=self.env != ENV_DEV,
            verify_certs=self.env != ENV_DEV,
            connection_class=RequestsHttpConnection
        )

    def check_connection(self):
        try:
            self.client.ping()

            return 'OK'
        except Exception as error:
            logger.error(''.join(traceback.format_exception(None, error, error.__traceback__)))

    def create(self, index: str, doc_id: str, doc_source: dict):
        """
          Only creates the doc
          Returns a 409 response when a document with a same ID already exists in the index (TODO validate on local)
        """
        if not index or not doc_id or not doc_source:
            raise GenericException('Missing arguments for ES create.')

        self.client.index(
            index=index,
            id=doc_id,
            op_type='create',
            body=doc_source,
            timeout=self.request_timeout
        )

    def index(self, index: str, doc_id: str, doc_source: dict):
        """
          If doc with doc_id is not found, then creates. Else, replaces
        """
        if not index or not doc_id or not doc_source:
            raise GenericException('Missing arguments for ES index.')

        self.client.index(
            index=index,
            id=doc_id,
            op_type='index',
            body=doc_source,
            timeout=self.request_timeout
        )

    def update(self, index: str, doc_id: str, doc_source: dict):
        """
          If doc with doc_id is not found, then creates. Else, updates
          doc_source: Either partial doc or script
        """
        if not index or not doc_id or not doc_source:
            raise GenericException('Missing arguments for ES update.')

        self.client.update(
            index=index,
            id=doc_id,
            body=doc_source,
            retry_on_conflict=3
        )
        # TODO explore _source_includes to exclude fields that would never be updated by a script

    def update_by_query(self, index: str, doc_source: str):
        """
          If doc with doc_id is not found, then creates. Else, updates

          Example of body: {
              "script": {
                "source": "ctx._source.publisherName = 'Postman'",
                "lang": "painless"
              },
              "query": {
                "term": {
                  "publisherId": 42
                }
              }
            }
        """
        if not index or not doc_source:
            raise GenericException('Missing arguments for ES update_by_query.')

        self.client.index(
            index=index,
            body=doc_source,
            slices='auto'
        )
        # TODO explore requests_per_second

    def delete(self, index: str, doc_id: str):
        """
          Deletes the doc
        """
        if not index or not doc_id:
            raise GenericException('Missing arguments for ES delete.')

        self.client.index(
            index=index,
            id=doc_id,
            timeout=self.request_timeout
        )

    # TODO bulk

    def write(self, streams: List[SinkRecordDTO]) -> None:
        """
        Writes processed records read from kafka to Elastic search
        :param streams: List of SinkRecordDTO - transformed data to be written to ES
        :return: None

        Example of streams: [
            {
              key='551502',
              message={
                  '_id': 'team#551502,
                  'id': 551502,
                  'name': foo,
                  'description': bar,
              },
              topic=god.organizations,
              offset=0,
              sink_operation={
                  sink_operation_type: 'insert'
                  update_query: {}
                  source_field_name: None
                  new_val: None
                  target: teams_write
              },
              partition=1
            },
            {
              key='551502',
              message={
                '_id': 'team#551502,
                'id': 551502,
                'name': foo,
                'description': bar,
              },
              topic=god.organizations,
              offset=0,
              sink_operation={

              },
              partition=1
            }
        ]
        """
        for sink_record_dto in streams:
            logger.info(f'{sink_record_dto.key} : {sink_record_dto.message}')

            getattr(self, sink_record_dto.sink_operation.sink_operation_type.value)(
                index=sink_record_dto.sink_operation.target,
                doc_id=sink_record_dto.sink_operation.doc_id,
                doc_source=sink_record_dto.message
            )

    def close(self) -> None:
        try:
            self.client.transport.close()
        except BaseException as e:
            logger.error(f"Filed to close ES client {e}")
