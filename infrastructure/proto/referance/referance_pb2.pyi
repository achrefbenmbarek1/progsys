from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ["dataType", "method", "referance"]
    DATATYPE_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    REFERANCE_FIELD_NUMBER: _ClassVar[int]
    dataType: str
    method: str
    referance: str
    def __init__(self, referance: _Optional[str] = ..., dataType: _Optional[str] = ..., method: _Optional[str] = ...) -> None: ...
