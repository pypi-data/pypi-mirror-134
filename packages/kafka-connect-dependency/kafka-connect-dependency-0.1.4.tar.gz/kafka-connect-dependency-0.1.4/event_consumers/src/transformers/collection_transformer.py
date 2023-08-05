import json
from typing import List

from kafka.consumer.fetcher import ConsumerRecord

from event_consumers.src.model.worker_dto import SinkRecordDTO, SinkOperation, SinkOperationType
from event_consumers.src.transformers.transformer import StreamTransformer

collection_doc_id_prefix = 'collection#' # TODO move to config

class CollectionTransformer(StreamTransformer):
    def __init__(self, config: dict):
        super().__init__(config)
        self.event_op_dict = {
            'WriteRowsEvent': ['create_collection'],
            'UpdateRowsEvent': ['update_collection'],
            'DeleteRowsEvent': ['delete_collection']
        }

    def create_collection(self, message_dict: dict):
        message: dict = {
            'id': message_dict['id'].replace('#', '-'),
            'name': message_dict['name'],
            'description': message_dict['description'],
            'entityType': 'collection',
            'publisherType': 'team' if message_dict['team'] else 'user',
            'publisherId': message_dict['team'] if message_dict['team'] else message_dict['owner'],
            'createdAt': message_dict['createdAt'],
            'updatedAt': message_dict['updatedAt']
        }

        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.INSERT,
            target='collections_write',  # TODO move to config
            doc_id=collection_doc_id_prefix + message_dict['id'].replace('#', '-')
        )

        return message, sink_operation

    def update_collection(self, message_dict: dict):
        message: dict = {
            'doc': {
                'id': message_dict['id'].replace('#', '-'),
                'name': message_dict['name'],
                'description': message_dict['description'],
                'entityType': 'collection',
                'publisherType': 'team' if message_dict['team'] else 'user',
                'publisherId': message_dict['team'] if message_dict['team'] else message_dict[
                    'owner'],
                'createdAt': message_dict['createdAt'],
                'updatedAt': message_dict['updatedAt']
            },
            'doc_as_upsert': True
        }

        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.UPDATE,
            target='collections_write',  # TODO move to config
            doc_id=collection_doc_id_prefix + message_dict['id'].replace('#', '-')
        )

        return message, sink_operation

    def delete_collection(self, message_dict: dict):
        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.DELETE,
            target='collections_write',  # TODO move to config
            doc_id=collection_doc_id_prefix + message_dict['id'].replace('#', '-')
        )

        return None, sink_operation

    def transform(self, consumer_record: ConsumerRecord) -> List[SinkRecordDTO]:
        """
        converts message to message dict
        :param consumer_record: kafka consumer record
          Example key value pairs:
            key='551502#560ffd90-7080-462c-8714-0337a6c4c873',
            value={
              "id": "551502#560ffd90-7080-462c-8714-0337a6c4c873",
              "name": "Postman Echo collection in Newman Team2 workspace",
              "owner": "551502",
              "lastUpdatedBy": "551502",
              "lastRevision": 70984152,
              "team": "323806",
              "description": null,
              "remote_id": "0",
              "remoteLink": null,
              "folders_order": "[]",
              "order": "[\"d82151",
              "shared": null,
              "write": null,
              "createdAt": "2021-10-07 04:10:11",
              "updatedAt": "2021-10-07 04:10:12",
              "transactionId": "6542c609-5ffc-46c1-b5fb-d6fc319ec75d",
              "variables": null,
              "events": null,
              "auth": null,
              "_cdc_sequence_id": 17199321009770,
              "_cdc_type": "WriteRowsEvent",
              "_cdc_table": "collection",
              "_is_deleted": "True",
              "_batch_timestamp": "2021-10-07T04:11:41Z",
              "_sdc_extracted_at": "2021-10-07T04:11:41.755768"
            }
        :return: SinkRecordDTO
        """

        message_dict: dict = json.loads(consumer_record.value)

        # Do not process non-team and personal collections
        if not message_dict['team']:
            return []

        sink_record_dto_list: List[SinkRecordDTO] = []

        ops_list = self.event_op_dict[message_dict['_cdc_type']]

        for operation in ops_list:
            message, sink_operation = getattr(self, operation)(message_dict)

            sink_record_dto_list.append(SinkRecordDTO(key=consumer_record.key,
                                                      message=message,
                                                      topic=consumer_record.topic,
                                                      offset=consumer_record.offset,
                                                      sink_operation=sink_operation,
                                                      partition=consumer_record.partition))

        return sink_record_dto_list
