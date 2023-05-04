from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Facture(_message.Message):
    __slots__ = ["referance", "sommeAPayer"]
    REFERANCE_FIELD_NUMBER: _ClassVar[int]
    SOMMEAPAYER_FIELD_NUMBER: _ClassVar[int]
    referance: str
    sommeAPayer: str
    def __init__(self, referance: _Optional[str] = ..., sommeAPayer: _Optional[str] = ...) -> None: ...
