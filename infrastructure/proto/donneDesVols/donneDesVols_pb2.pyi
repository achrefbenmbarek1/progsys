from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Vol(_message.Message):
    __slots__ = ["destination", "nombreDePlaceDispo", "prix", "referance"]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    NOMBREDEPLACEDISPO_FIELD_NUMBER: _ClassVar[int]
    PRIX_FIELD_NUMBER: _ClassVar[int]
    REFERANCE_FIELD_NUMBER: _ClassVar[int]
    destination: str
    nombreDePlaceDispo: int
    prix: float
    referance: str
    def __init__(self, referance: _Optional[str] = ..., destination: _Optional[str] = ..., nombreDePlaceDispo: _Optional[int] = ..., prix: _Optional[float] = ...) -> None: ...
