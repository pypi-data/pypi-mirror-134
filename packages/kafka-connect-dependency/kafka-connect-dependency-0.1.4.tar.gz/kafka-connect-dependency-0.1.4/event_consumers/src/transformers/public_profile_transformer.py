import json
from typing import List

from kafka.consumer.fetcher import ConsumerRecord

from event_consumers.src.model.worker_dto import SinkRecordDTO, SinkOperation, SinkOperationType
from event_consumers.src.transformers.transformer import StreamTransformer

class PublicProfileTransformer(StreamTransformer):
    def __init__(self, config: dict):
        super().__init__(config)
        self.event_op_dict = {
            'WriteRowsEvent': [],
            'UpdateRowsEvent': ['update_team', 'update_collection', 'update_workspace', 'update_api'],
            'DeleteRowsEvent': []
        }

    def update_team(self, message_dict: dict):
        return

    def update_collection(self, message_dict: dict):
        return

    def update_api(self, message_dict: dict):
        return

    def update_workspace(self, message_dict: dict):
        return

    def transform(self, consumer_record: ConsumerRecord) -> List[SinkRecordDTO]:
        """
        converts message to message dict
        Example key value pairs:
            key=141278,
            value={
                "id": 141278,
                "entity_id": 839906,
                "entity_type": "user",
                "handle": "free596326",
                "is_public": 1,
                "is_compliant": 1,
                "created_at": "2021-12-14 08:15:08",
                "updated_at": "2021-12-14 08:15:08",
                "_cdc_sequence_id": 1639469722643302,
                "_cdc_type": "WriteRowsEvent",
                "_cdc_table": "public_profile",
                "_is_deleted": false,
                "_batch_timestamp": "2021-12-14T08:15:22Z",
                "_sdc_extracted_at": "2021-12-14T08:15:22.643528"
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
