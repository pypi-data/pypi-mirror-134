import json
from typing import List

from kafka.consumer.fetcher import ConsumerRecord

from event_consumers.src.model.worker_dto import SinkRecordDTO, SinkOperation, SinkOperationType
from event_consumers.src.transformers.transformer import StreamTransformer

collection_doc_id_prefix = 'collection#' # TODO move to config

class RequestTransformer(StreamTransformer):
    def __init__(self, config: dict):
        super().__init__(config)
        self.event_op_dict = {
            'WriteRowsEvent': ['add_request'],
            'UpdateRowsEvent': ['update_request'],
            'DeleteRowsEvent': ['remove_request']
        }

    def add_request(self, message_dict: dict):
        """
        This is a strict update on collection, not an upsert.
        TODO Trying to add request to missing collection will raise an exception.
        error.type: "document_missing_exception", status: 404
        In that case, there should be a retry
        Same holds for response and folder
        """
        message: dict = {
            "script": {
                "source": "ctx._source.requests.add(params.request)",
                "lang": "painless",
                "params": {
                    "request": {
                        'id': message_dict.id,
                        'name': message_dict.name,
                        'description': message_dict.description,
                        'url': message_dict.url,
                        'method': message_dict.method
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

    def update_request(self, message_dict: dict):
        """
        This is a strict update on collection, not an upsert.
        TODO Trying to update request on missing collection will raise an exception.
        In that case, there should be a retry
        Same holds for response and folder
        """
        message: dict = {
            "script": {
                "source": """
                    for (int i = 0; i < ctx._source.requests.length; ++i) {
                        if (ctx._source.requests[i]['id'] == params.request.id) {
                            ctx._source.requests[i] = params.request;
                            break;
                        }
                    }
                """,
                "lang": "painless",
                "params": {
                    "request": {
                        'id': message_dict.id,
                        'name': message_dict.name,
                        'description': message_dict.description,
                        'url': message_dict.url,
                        'method': message_dict.method
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

    def remove_request(self, message_dict: dict):
        """
        This is a strict update on collection, not an upsert.
        TODO Trying to update request on missing collection will raise an exception.
        In that case, there should be a retry
        Same holds for response and folder
        """
        message: dict = {
            "script": {
                "source": """
                    for (int i = 0; i < ctx._source.requests.length; ++i) {
                        if (ctx._source.requests[i]['id'] == params.request.id) {
                            ctx._source.requests.remove(i);
                            break;
                        }
                    }
                """,
                "lang": "painless",
                "params": {
                    "request": {
                        'id': message_dict['id']
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
              "id": "637845#d30a351e-abd4-4a6b-b5ce-cccf3737c846",
              "name": "New Request",
              "dataMode": null,
              "data": null,
              "rawModeData": null,
              "descriptionFormat": null,
              "description": null,
              "headers": "",
              "method": "GET",
              "pathVariables": null,
              "url": "",
              "preRequestScript": null,
              "tests": null,
              "currentHelper": null,
              "helperAttributes": null,
              "queryParams": "[]",
              "headerData": "[]",
              "pathVariableData": "[]",
              "owner": "637845",
              "lastUpdatedBy": "637845",
              "lastRevision": null,
              "folder": null,
              "collection": "637845#f6980514-24f9-4dfd-b7dd-03196d4c61d9",
              "createdAt": "2021-11-24 07:57:40",
              "updatedAt": "2021-11-24 07:57:40",
              "transactionId": "01776d7c-358f-49f3-8bdc-21f811ae9715",
              "variables": null,
              "events": null,
              "auth": null,
              "variables2": null,
              "variables3": null,
              "protocolProfileBehavior": null,
              "dataDisabled": null,
              "graphqlModeData": null,
              "responses_order": "[]",
              "_cdc_sequence_id": 1637742344855914,
              "_cdc_type": "WriteRowsEvent",
              "_cdc_table": "request",
              "_is_deleted": false,
              "_batch_timestamp": "2021-11-24T08:25:44Z",
              "_sdc_extracted_at": "2021-11-24T08:25:44.856273"
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
