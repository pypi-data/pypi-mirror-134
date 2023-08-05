import json
from typing import List

from kafka.consumer.fetcher import ConsumerRecord

from event_consumers.src.model.worker_dto import SinkRecordDTO, SinkOperation, SinkOperationType
from event_consumers.src.transformers.transformer import StreamTransformer

class EntityImagesTransformer(StreamTransformer):
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
            key='188271', # TODO need to check if key will be string if unique id in table is integer
            value={
                "id": 188271,
                "entity_type": "user",
                "entity_id": 839906,
                "image_type": "hero",
                "image_url": "https://res.cloudinary.com/ddn1d7iih/image/upload/t_user_hero/v1/user_hero/def-hero-image",
                "is_default": 1,
                "created_at": "2021-12-14 08:15:08",
                "updated_at": "2021-12-14 08:15:08",
                "_cdc_sequence_id": 1639469722639249,
                "_cdc_type": "WriteRowsEvent",
                "_cdc_table": "entity_images",
                "_is_deleted": false,
                "_batch_timestamp": "2021-12-14T08:15:22Z",
                "_sdc_extracted_at": "2021-12-14T08:15:22.639489"
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
