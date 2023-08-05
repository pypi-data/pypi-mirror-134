import json
from typing import List

from kafka.consumer.fetcher import ConsumerRecord

from event_consumers.src.model.worker_dto import SinkRecordDTO, SinkOperation, SinkOperationType
from event_consumers.src.transformers.transformer import StreamTransformer

class ForkTransformer(StreamTransformer):
    def __init__(self, config: dict):
        super().__init__(config)
        self.event_op_dict = {
            'WriteRowsEvent': ['update_collection'],
            'UpdateRowsEvent': ['update_collection'],
            'DeleteRowsEvent': ['update_collection']
        }

    def update_collection(self, message_dict: dict):
        return

    def transform(self, consumer_record: ConsumerRecord) -> List[SinkRecordDTO]:
        """
        converts message to message dict
        :param consumer_record: kafka consumer record
          Example key value pairs:
            key='20789',
            value={
                "id": 20789,
                "name": "abc copy forked",
                "model": "collection",
                "fromId": "118680#1b95a613-00d6-4a43-a71a-0d1a8e81c0d3",
                "toId": "118680#194c1051-765e-40f6-8793-c29aa8f827fc",
                "revision": 74140379,
                "createdAt": "2021-12-14 21:12:47",
                "updatedAt": "2021-12-14 21:12:47",
                "deletedAt": null,
                "createdBy": "118680",
                "transactionId": "c77a7848-572d-40ad-8d97-85c7aeecf2d0",
                "keyframe": 7707,
                "keyframeType": "reference",
                "isParentAhead": null,
                "isForkAhead": null,
                "_cdc_sequence_id": 1639516368980319,
                "_cdc_type": "WriteRowsEvent",
                "_cdc_table": "fork",
                "_is_deleted": false,
                "_batch_timestamp": "2021-12-14T21:12:48Z",
                "_sdc_extracted_at": "2021-12-14T21:12:48.980794"
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
