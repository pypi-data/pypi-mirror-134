import json
from typing import List

from kafka.consumer.fetcher import ConsumerRecord

from event_consumers.src.model.worker_dto import SinkRecordDTO, SinkOperation, SinkOperationType
from event_consumers.src.transformers.transformer import StreamTransformer

def update_by_query_payload(message_dict: dict) -> dict:
        return {
            'script': {
                'source': "ctx._source.publisherName = %s" % message_dict['name'],
                'lang': 'painless'
            },
            'query': {
                'bool': {
                    'filter': {
                        'bool': {
                            'must': [
                                {
                                    'term': {
                                        'publisherId': message_dict['id']
                                    }
                                },
                                {
                                    'term': {
                                        'publisherType': 'user'
                                    }
                                }
                            ]
                        }
                    }
                }
            }
        }

class UsersTransformer(StreamTransformer):
    def __init__(self, config: dict):
        super().__init__(config)
        self.event_op_dict = {
            'WriteRowsEvent': [],
            'UpdateRowsEvent': ['update_collection', 'update_workspace', 'update_api'],
            'DeleteRowsEvent': []
        }

    def update_collection(self, message_dict: dict):
        message: dict = update_by_query_payload(message_dict)

        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.UPDATE_BY_QUERY,
            target='collections_write'  # TODO move to config
        )

        return message, sink_operation

    def update_api(self, message_dict: dict):
        message: dict = update_by_query_payload(message_dict)

        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.UPDATE_BY_QUERY,
            target='apis_write'  # TODO move to config
        )

        return message, sink_operation

    def update_workspace(self, message_dict: dict):
        message: dict = update_by_query_payload(message_dict)

        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.UPDATE_BY_QUERY,
            target='workspaces_write'  # TODO move to config
        )

        return message, sink_operation

    def transform(self, consumer_record: ConsumerRecord) -> List[SinkRecordDTO]:
        """
        converts message to message dict
        Example key value pairs:
            key='839892',
            value={
                "id": 839892,
                "username": "free865624",
                "email": "free865624@lorem.ipsum",
                "email_domain": "lorem.ipsum",
                "google_id": null,
                "password": "$2y$10$OyTOdcIDdjOzfvB2TajDYusUxb6/88nBPkee2WPaK2jMOFD9mMSIq",
                "created_at": "2021-12-14 06:02:42",
                "updated_at": "1970-01-01 00:00:00",
                "name": null,
                "given_name": null,
                "family_name": null,
                "picture": null,
                "gender": null,
                "birthday": null,
                "locale": null,
                "link": null,
                "role": "user",
                "sync_invited": 1,
                "sync_eula_accepted": 1,
                "base_eula_accepted": 0,
                "latest_version": null,
                "disabled_sync": 0,
                "ghost": 0,
                "meta": null,
                "enabled": 1,
                "email_verified": 0,
                "pro_dashboard_enabled": 0,
                "api_version": 1,
                "transactionId": null,
                "marketing_updates_enabled": 1,
                "description": null,
                "_cdc_sequence_id": 1639461803653701,
                "_cdc_type": "DeleteRowsEvent",
                "_cdc_table": "users",
                "_is_deleted": true,
                "_batch_timestamp": "2021-12-14T06:03:23Z",
                "_sdc_extracted_at": "2021-12-14T06:03:23.654133"
            }
        :param consumer_record: kafka consumer record
        :return: SinkRecordDTO
        """

        message_dict: dict = json.loads(consumer_record.value)
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
