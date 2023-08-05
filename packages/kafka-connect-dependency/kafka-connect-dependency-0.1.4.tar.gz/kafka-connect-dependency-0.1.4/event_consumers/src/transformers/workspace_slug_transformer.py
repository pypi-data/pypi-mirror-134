import json
from typing import List

from kafka.consumer.fetcher import ConsumerRecord

from event_consumers.src.model.worker_dto import SinkRecordDTO, SinkOperation, SinkOperationType
from event_consumers.src.transformers.transformer import StreamTransformer

workspace_doc_id_prefix = 'workspace#' # TODO move to config

class WorkspaceTransformer(StreamTransformer):
    def __init__(self, config: dict):
        super().__init__(config)
        self.event_op_dict = {
            'WriteRowsEvent': ['update_workspace'],
            'UpdateRowsEvent': ['update_workspace', 'update_collection', 'update_api'],
            'DeleteRowsEvent': ['update_workspace']
        }

    def update_workspace(self, message_dict: dict):
        return

    def update_collection(self, message_dict: dict):
        return

    def update_api(self, message_dict: dict):
        return

    def transform(self, consumer_record: ConsumerRecord) -> List[SinkRecordDTO]:
        """
        converts message to message dict
        :param consumer_record: kafka consumer record
          Example key value pairs:
            key='148256',
            value={
                "id": 148256,
                "workspaceId": "42e34baa-e326-4150-abc7-919054c78565",
                "slug": "test",
                "entityType": "team",
                "entityId": "340252",
                "publishedBy": "814243",
                "transactionId": "f74f9e13-449b-4315-9115-212546612aff",
                "createdAt": "2021-12-15 11:02:30",
                "updatedAt": "2021-12-15 11:02:30",
                "_cdc_sequence_id": 1639566153103617,
                "_cdc_type": "WriteRowsEvent",
                "_cdc_table": "workspace_slug",
                "_is_deleted": false,
                "_batch_timestamp": "2021-12-15T11:02:33Z",
                "_sdc_extracted_at": "2021-12-15T11:02:33.104116"
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
