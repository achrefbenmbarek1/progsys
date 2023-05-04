from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ElementOfTransactionHistory(_message.Message):
    __slots__ = ["referanceVol", "referenceAgence", "resultat", "transaction", "valeur"]
    REFERANCEVOL_FIELD_NUMBER: _ClassVar[int]
    REFERENCEAGENCE_FIELD_NUMBER: _ClassVar[int]
    RESULTAT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    VALEUR_FIELD_NUMBER: _ClassVar[int]
    referanceVol: str
    referenceAgence: str
    resultat: str
    transaction: str
    valeur: int
    def __init__(self, referanceVol: _Optional[str] = ..., referenceAgence: _Optional[str] = ..., transaction: _Optional[str] = ..., valeur: _Optional[int] = ..., resultat: _Optional[str] = ...) -> None: ...

class EntireTransactionHistory(_message.Message):
    __slots__ = ["transactionHistory"]
    TRANSACTIONHISTORY_FIELD_NUMBER: _ClassVar[int]
    transactionHistory: _containers.RepeatedCompositeFieldContainer[ElementOfTransactionHistory]
    def __init__(self, transactionHistory: _Optional[_Iterable[_Union[ElementOfTransactionHistory, _Mapping]]] = ...) -> None: ...
