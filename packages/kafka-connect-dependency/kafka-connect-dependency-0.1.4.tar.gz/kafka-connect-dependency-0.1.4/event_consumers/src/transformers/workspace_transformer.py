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
            'WriteRowsEvent': ['create_workspace'],
            'UpdateRowsEvent': ['update_workspace', 'update_collection', 'update_api'],
            'DeleteRowsEvent': ['delete_workspace']
        }

    def create_workspace(self, message_dict: dict):
        message: dict = {
            'id': message_dict['id'],
            'name': message_dict['name'],
            'summary': message_dict['summary'],
            'description': message_dict['description'],
            'publisherType': 'team' if message_dict['team'] else 'user',
            'publisherId': message_dict['team'] if message_dict['team'] else message_dict['createdBy'],
            'createdAt': message_dict['createdAt'],
            'updatedAt': message_dict['updatedAt']
        }

        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.INSERT,
            target='workspaces_write',  # TODO move to config
            doc_id=workspace_doc_id_prefix + message_dict['id']
        )

        return message, sink_operation

    def update_workspace(self, message_dict: dict):
        message: dict = {
            'doc': {
                'id': message_dict['id'],
                'name': message_dict['name'],
                'summary': message_dict['summary'],
                'description': message_dict['description'],
                'publisherType': 'team' if message_dict['team'] else 'user',
                'publisherId': message_dict['team'] if message_dict['team'] else message_dict['createdBy'],
                'createdAt': message_dict['createdAt'],
                'updatedAt': message_dict['updatedAt']
            },
            'doc_as_upsert': True
        }

        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.UPDATE,
            target='workspaces_write',  # TODO move to config
            doc_id=workspace_doc_id_prefix + message_dict['id']
        )

        return message, sink_operation

    def update_collection(self, message_dict: dict):
        return

    def update_api(self, message_dict: dict):
        return

    def delete_workspace(self, message_dict: dict):
        sink_operation = SinkOperation(
            sink_operation_type=SinkOperationType.DELETE,
            target='workspaces_write',  # TODO move to config
            doc_id=workspace_doc_id_prefix + message_dict['id']
        )

        return None, sink_operation

    def transform(self, consumer_record: ConsumerRecord) -> List[SinkRecordDTO]:
        """
        converts message to message dict
        :param consumer_record: kafka consumer record
          Example key value pairs:
            key='79b4ae96-6241-4b38-80e0-25297b6f043a',
            value={
                "id": "79b4ae96-6241-4b38-80e0-25297b6f043a",
                "name": "Team Workspace",
                "description": "This is ",
                "summary": null,
                "team": "344348",
                "createdBy": "790309",
                "transactionId": "7ff2224f-3944-4453-bede-fb37852ac170",
                "updatedBy": "790309",
                "isDeleted": 0, TODO handle this
                "createdAt": "2021-12-13 09:53:03",
                "updatedAt": "2021-12-13 09:53:03",
                "visibilityStatus": 2,
                "autoId": 290978,
                "_cdc_sequence_id": 1639389199361456,
                "_cdc_type": "WriteRowsEvent",
                "_cdc_table": "workspace",
                "_is_deleted": false,
                "_batch_timestamp": "2021-12-13T09:53:19Z",
                "_sdc_extracted_at": "2021-12-13T09:53:19.361929"
              }
        :return: SinkRecordDTO
        """

        message_dict: dict = json.loads(consumer_record.value)

        # Do not process non-team and personal workspaces
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
