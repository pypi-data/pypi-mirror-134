from enum import Enum
from typing import Optional, Dict

from pydantic import BaseModel


class SinkOperationType(Enum):
    UPDATE = 'update'
    DELETE = 'delete'
    INSERT = 'create'
    UPDATE_BY_QUERY = 'update_by_query'


class SinkOperation(BaseModel):
    sink_operation_type: SinkOperationType

    # update query for update by query
    update_query: Dict = {}

    # source field name for script-based update
    source_field_name: Optional[str]

    # this can be a json or any primitive value
    new_val: object = None

    # target index
    target: str

    # doc unique identifier
    doc_id: str

    class Config:
        arbitrary_types_allowed = True


class SinkRecordDTO(BaseModel):
    sink_operation: SinkOperation
    message: Dict
    key: Optional[str]
    offset: Optional[int]
    topic: Optional[str]
    partition: Optional[int]


class DeadLetterDTO(BaseModel):
    key: str
    message: str
    topic: str
    partition: int
    failed_at: str
    error: str
    offset: int
