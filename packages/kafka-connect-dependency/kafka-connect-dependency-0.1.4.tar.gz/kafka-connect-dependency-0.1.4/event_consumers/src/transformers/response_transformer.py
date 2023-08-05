import json
from typing import List

from kafka.consumer.fetcher import ConsumerRecord

from event_consumers.src.model.worker_dto import SinkRecordDTO, SinkOperation, SinkOperationType
from event_consumers.src.transformers.transformer import StreamTransformer

collection_doc_id_prefix = 'collection#' # TODO move to config

class ResponseTransformer(StreamTransformer):
    def __init__(self, config: dict):
        super().__init__(config)
        self.event_op_dict = {
            'WriteRowsEvent': ['add_response'], # TODO can be generalized to child based operation
            'UpdateRowsEvent': ['update_response'],
            'DeleteRowsEvent': ['remove_response']
        }

    def add_response(self, message_dict: dict):
        """
        This is a strict update on collection, not an upsert.
        """
        message: dict = {
            "script": {
                "source": "ctx._source.responses.add(params.response)",
                "lang": "painless",
                "params": {
                    "response": {
                        'id': message_dict.id,
                        'name': message_dict.name
                    }
                }
            }
        }

        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.UPDATE,
            target='collections_write',  # TODO move to config
            doc_id=collection_doc_id_prefix + message_dict.collection.replace('#', '-')
        )

        return message, sink_operation

    def update_response(self, message_dict: dict):
        """
        This is a strict update on collection, not an upsert.
        """
        message: dict = {
            "script": {
                "source": """
                    for (int i = 0; i < ctx._source.responses.length; ++i) {
                        if (ctx._source.responses[i]['id'] == params.response.id) {
                            ctx._source.responses[i] = params.response;
                            break;
                        }
                    }
                """,
                "lang": "painless",
                "params": {
                    "response": {
                        'id': message_dict.id,
                        'name': message_dict.name
                    }
                }
            }
        }

        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.UPDATE,
            target='collections_write',  # TODO move to config
            doc_id=collection_doc_id_prefix + message_dict.collection.replace('#', '-')
        )

        return message, sink_operation

    def remove_response(self, message_dict: dict):
        """
        This is a strict update on collection, not an upsert.
        """
        message: dict = {
            "script": {
                "source": """
                    for (int i = 0; i < ctx._source.responses.length; ++i) {
                        if (ctx._source.responses[i]['id'] == params.response.id) {
                            ctx._source.responses.remove(i);
                            break;
                        }
                    }
                """,
                "lang": "painless",
                "params": {
                    "response": {
                        'id': message_dict.id
                    }
                }
            }
        }

        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.UPDATE,
            target='collections_write',  # TODO move to config
            doc_id=collection_doc_id_prefix + message_dict.collection.replace('#', '-')
        )

        return message, sink_operation

    def transform(self, consumer_record: ConsumerRecord) -> List[SinkRecordDTO]:
        """
        converts message to message dict
        :param consumer_record: kafka consumer record
          Example key value pairs:
            key='637845#d30a351e-abd4-4a6b-b5ce-cccf3737c846',
            value={
                "id": "448927#6792f142-da00-4b07-a7c7-2b466a4aeb43",
                "owner": "448927",
                "lastUpdatedBy": "448927",
                "lastRevision": null,
                "request": "448927#f0ec14c6-3a2a-4a1e-b4c5-a4a34c831b0c",
                "name": "200",
                "status": "OK",
                "responseCode": "{\"code\":",
                "time": "616",
                "headers": "[{\"key\":",
                "cookies": "[]",
                "mime": null,
                "text": "{\n  \"arg",
                "language": "json",
                "rawDataType": "text",
                "state": null,
                "previewType": null,
                "searchResultScrolledTo": null,
                "version": null,
                "requestObject": "{\"id\":\"1",
                "createdAt": "2021-12-15 06:30:05",
                "updatedAt": "2021-12-15 06:30:05",
                "transactionId": "fcd94e37-0e2f-46e5-86c5-d879400f2bef",
                "_cdc_sequence_id": 1639549814522738,
                "_cdc_type": "WriteRowsEvent",
                "_cdc_table": "response",
                "_is_deleted": false,
                "_batch_timestamp": "2021-12-15T06:30:14Z",
                "_sdc_extracted_at": "2021-12-15T06:30:14.526361"
            }
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
