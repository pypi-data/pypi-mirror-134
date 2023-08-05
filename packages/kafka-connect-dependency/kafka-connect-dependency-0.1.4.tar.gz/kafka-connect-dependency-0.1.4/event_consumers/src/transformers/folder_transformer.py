import json
from typing import List

from kafka.consumer.fetcher import ConsumerRecord

from event_consumers.src.model.worker_dto import SinkRecordDTO, SinkOperation, SinkOperationType
from event_consumers.src.transformers.transformer import StreamTransformer

collection_doc_id_prefix = 'collection#'

class FolderTransformer(StreamTransformer):
    def __init__(self, config: dict):
        super().__init__(config)
        self.event_op_dict = {
            'WriteRowsEvent': ['add_folder'], # TODO can be generalized to child based operation
            'UpdateRowsEvent': ['update_folder'],
            'DeleteRowsEvent': ['remove_folder']
        }

    def add_folder(self, message_dict: dict):
        """
        This is a strict update on collection, not an upsert.
        """
        message: dict = {
            "script": {
                "source": "ctx._source.folders.add(params.folder)",
                "lang": "painless",
                "params": {
                    "folder": {
                        'id': message_dict.id,
                        'name': message_dict.name,
                        'description': message_dict.description
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

    def update_folder(self, message_dict: dict):
        """
        This is a strict update on collection, not an upsert.
        """
        message: dict = {
            "script": {
                "source": """
                    for (int i = 0; i < ctx._source.folders.length; ++i) {
                        if (ctx._source.folders[i]['id'] == params.folder.id) {
                            ctx._source.folders[i] = params.folder;
                            break;
                        }
                    }
                """,
                "lang": "painless",
                "params": {
                    "folder": {
                        'id': message_dict.id,
                        'name': message_dict.name,
                        'description': message_dict.description
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

    def remove_folder(self, message_dict: dict):
        """
        This is a strict update on collection, not an upsert.
        """
        message: dict = {
            "script": {
                "source": """
                    for (int i = 0; i < ctx._source.folders.length; ++i) {
                        if (ctx._source.folders[i]['id'] == params.folder.id) {
                            ctx._source.folders.remove(i);
                            break;
                        }
                    }
                """,
                "lang": "painless",
                "params": {
                    "folder": {
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
            key='118680#e5e48ac6-f6c5-4187-b06e-d0f2a8ca2bad',
            value={
                "id": "118680#e5e48ac6-f6c5-4187-b06e-d0f2a8ca2bad",
                "name": "them",
                "description": null,
                "owner": "118680",
                "lastUpdatedBy": "118680",
                "lastRevision": null,
                "collection": "118680#194c1051-765e-40f6-8793-c29aa8f827fc",
                "folder": null,
                "order": "[]",
                "folders_order": "[]",
                "createdAt": "2021-12-14 21:12:47",
                "updatedAt": "2021-12-14 21:12:47",
                "transactionId": "c77a7848-572d-40ad-8d97-85c7aeecf2d0",
                "variables": null,
                "events": null,
                "auth": null,
                "_cdc_sequence_id": 1639516368996949,
                "_cdc_type": "WriteRowsEvent",
                "_cdc_table": "folder",
                "_is_deleted": false,
                "_batch_timestamp": "2021-12-14T21:12:48Z",
                "_sdc_extracted_at": "2021-12-14T21:12:48.997940"
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
