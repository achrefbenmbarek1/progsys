# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transactionHistory.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18transactionHistory.proto\"\x83\x01\n\x1b\x45lementOfTransactionHistory\x12\x14\n\x0creferanceVol\x18\x01 \x01(\t\x12\x17\n\x0freferenceAgence\x18\x02 \x01(\t\x12\x13\n\x0btransaction\x18\x03 \x01(\t\x12\x0e\n\x06valeur\x18\x04 \x01(\x05\x12\x10\n\x08resultat\x18\x05 \x01(\t\"T\n\x18\x45ntireTransactionHistory\x12\x38\n\x12transactionHistory\x18\x01 \x03(\x0b\x32\x1c.ElementOfTransactionHistoryb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transactionHistory_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ELEMENTOFTRANSACTIONHISTORY._serialized_start=29
  _ELEMENTOFTRANSACTIONHISTORY._serialized_end=160
  _ENTIRETRANSACTIONHISTORY._serialized_start=162
  _ENTIRETRANSACTIONHISTORY._serialized_end=246
# @@protoc_insertion_point(module_scope)
