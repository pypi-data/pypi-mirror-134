import json
from typing import List

from kafka.consumer.fetcher import ConsumerRecord

from event_consumers.src.model.worker_dto import SinkRecordDTO, SinkOperation, SinkOperationType
from event_consumers.src.transformers.transformer import StreamTransformer

api_doc_id_prefix = 'api#'  # TODO move to config


class APITransformer(StreamTransformer):
    def __init__(self, config: dict):
        super().__init__(config)
        self.event_op_dict = {
            'WriteRowsEvent': ['create_api'],
            'UpdateRowsEvent': ['update_api'],
            'DeleteRowsEvent': ['delete_api']
        }

    def create_api(self, message_dict: dict):
        message: dict = {
            'id': message_dict['id'],
            'name': message_dict['name'],
            'summary': message_dict['summary'],
            'description': message_dict['description'],
            'publisherType': 'team' if message_dict['team'] else 'user',
            'publisherId': message_dict['team'] if message_dict['team'] else message_dict[
                'createdBy'],
            'createdAt': message_dict['createdAt'],
            'updatedAt': message_dict['updatedAt']
        }

        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.INSERT,
            target='apis_write',  # TODO move to config
            doc_id=api_doc_id_prefix + message_dict['id']
        )

        return message, sink_operation

    def update_api(self, message_dict: dict):
        message: dict = {
            'doc': {
                'id': message_dict['id'],
                'name': message_dict['name'],
                'summary': message_dict['summary'],
                'description': message_dict['description'],
                'publisherType': 'team' if message_dict['team'] else 'user',
                'publisherId': message_dict['team'] if message_dict['team'] else message_dict[
                    'createdBy'],
                'createdAt': message_dict['createdAt'],
                'updatedAt': message_dict['updatedAt']
            },
            'doc_as_upsert': True
        }

        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.UPDATE,
            target='apis_write',  # TODO move to config
            doc_id=api_doc_id_prefix + message_dict['id']
        )

        return message, sink_operation

    def delete_api(self, message_dict: dict):
        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.DELETE,
            target='apis_write',  # TODO move to config
            doc_id=api_doc_id_prefix + message_dict['id']
        )

        return None, sink_operation

    def transform(self, consumer_record: ConsumerRecord) -> List[SinkRecordDTO]:
        """
        converts message to message dict
        :param consumer_record: kafka consumer record
          Example key value pairs:
            key='fd9eb95b-4fd5-48da-85e1-6f38847a1b31',
            value={
                "id": "fd9eb95b-4fd5-48da-85e1-6f38847a1b31",
                "name": "git api 641103c4-7b33-4545-bdd3-14d9b65433ce",
                "summary": "git api summary",
                "description": "git api description",
                "createdBy": "559126",
                "updatedBy": "559126",
                "team": null,
                "lastRevision": null,
                "createdAt": "2021-11-09 08:32:20",
                "updatedAt": "2021-11-09 08:32:20",
                "transactionId": "d87212d0-1b71-4fb5-a16c-13856b6d8dd8",
                "_cdc_sequence_id": 1636446747888440,
                "_cdc_type": "WriteRowsEvent",
                "_cdc_table": "api",
                "_is_deleted": false,
                "_batch_timestamp": "2021-11-09T08:32:27Z",
                "_sdc_extracted_at": "2021-11-09T08:32:27.888775"
            }
        :return: SinkRecordDTO
        """

        message_dict: dict = json.loads(consumer_record.value)

        # Do not process non-team and personal apis
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
