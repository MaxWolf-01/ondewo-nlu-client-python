# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/nlu/operations.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ondewo.nlu import operation_metadata_pb2 as ondewo_dot_nlu_dot_operation__metadata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bondewo/nlu/operations.proto\x12\nondewo.nlu\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x17google/rpc/status.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a#ondewo/nlu/operation_metadata.proto\"\xa8\x01\n\tOperation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x08metadata\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04\x64one\x18\x03 \x01(\x08\x12#\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x12.google.rpc.StatusH\x00\x12(\n\x08response\x18\x05 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x08\n\x06result\"#\n\x13GetOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x93\x01\n\x15ListOperationsRequest\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x35\n\x10operation_filter\x18\x05 \x01(\x0b\x32\x1b.ondewo.nlu.OperationFilter\"\xb8\x02\n\x0fOperationFilter\x12\x17\n\x0fproject_parents\x18\x01 \x03(\t\x12\x36\n\x08statuses\x18\x02 \x03(\x0e\x32$.ondewo.nlu.OperationMetadata.Status\x12:\n\x05types\x18\x03 \x03(\x0e\x32+.ondewo.nlu.OperationMetadata.OperationType\x12\x30\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12.\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01\x12\x10\n\x08user_ids\x18\x06 \x03(\tB\x12\n\x10start_time_oneofB\x10\n\x0e\x65nd_time_oneof\"\\\n\x16ListOperationsResponse\x12)\n\noperations\x18\x01 \x03(\x0b\x32\x15.ondewo.nlu.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"&\n\x16\x43\x61ncelOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"&\n\x16\x44\x65leteOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t2\xda\x03\n\nOperations\x12v\n\x0eListOperations\x12!.ondewo.nlu.ListOperationsRequest\x1a\".ondewo.nlu.ListOperationsResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/{name=operations}\x12h\n\x0cGetOperation\x12\x1f.ondewo.nlu.GetOperationRequest\x1a\x15.ondewo.nlu.Operation\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/{name=operations/**}\x12o\n\x0f\x44\x65leteOperation\x12\".ondewo.nlu.DeleteOperationRequest\x1a\x16.google.protobuf.Empty\" \x82\xd3\xe4\x93\x02\x1a*\x18/v1/{name=operations/**}\x12y\n\x0f\x43\x61ncelOperation\x12\".ondewo.nlu.CancelOperationRequest\x1a\x16.google.protobuf.Empty\"*\x82\xd3\xe4\x93\x02$\"\x1f/v1/{name=operations/**}:cancel:\x01*b\x06proto3')



_OPERATION = DESCRIPTOR.message_types_by_name['Operation']
_GETOPERATIONREQUEST = DESCRIPTOR.message_types_by_name['GetOperationRequest']
_LISTOPERATIONSREQUEST = DESCRIPTOR.message_types_by_name['ListOperationsRequest']
_OPERATIONFILTER = DESCRIPTOR.message_types_by_name['OperationFilter']
_LISTOPERATIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListOperationsResponse']
_CANCELOPERATIONREQUEST = DESCRIPTOR.message_types_by_name['CancelOperationRequest']
_DELETEOPERATIONREQUEST = DESCRIPTOR.message_types_by_name['DeleteOperationRequest']
Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {
  'DESCRIPTOR' : _OPERATION,
  '__module__' : 'ondewo.nlu.operations_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.Operation)
  })
_sym_db.RegisterMessage(Operation)

GetOperationRequest = _reflection.GeneratedProtocolMessageType('GetOperationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOPERATIONREQUEST,
  '__module__' : 'ondewo.nlu.operations_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.GetOperationRequest)
  })
_sym_db.RegisterMessage(GetOperationRequest)

ListOperationsRequest = _reflection.GeneratedProtocolMessageType('ListOperationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTOPERATIONSREQUEST,
  '__module__' : 'ondewo.nlu.operations_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.ListOperationsRequest)
  })
_sym_db.RegisterMessage(ListOperationsRequest)

OperationFilter = _reflection.GeneratedProtocolMessageType('OperationFilter', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONFILTER,
  '__module__' : 'ondewo.nlu.operations_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.OperationFilter)
  })
_sym_db.RegisterMessage(OperationFilter)

ListOperationsResponse = _reflection.GeneratedProtocolMessageType('ListOperationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTOPERATIONSRESPONSE,
  '__module__' : 'ondewo.nlu.operations_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.ListOperationsResponse)
  })
_sym_db.RegisterMessage(ListOperationsResponse)

CancelOperationRequest = _reflection.GeneratedProtocolMessageType('CancelOperationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELOPERATIONREQUEST,
  '__module__' : 'ondewo.nlu.operations_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.CancelOperationRequest)
  })
_sym_db.RegisterMessage(CancelOperationRequest)

DeleteOperationRequest = _reflection.GeneratedProtocolMessageType('DeleteOperationRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEOPERATIONREQUEST,
  '__module__' : 'ondewo.nlu.operations_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.nlu.DeleteOperationRequest)
  })
_sym_db.RegisterMessage(DeleteOperationRequest)

_OPERATIONS = DESCRIPTOR.services_by_name['Operations']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OPERATIONS.methods_by_name['ListOperations']._options = None
  _OPERATIONS.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002\027\022\025/v1/{name=operations}'
  _OPERATIONS.methods_by_name['GetOperation']._options = None
  _OPERATIONS.methods_by_name['GetOperation']._serialized_options = b'\202\323\344\223\002\032\022\030/v1/{name=operations/**}'
  _OPERATIONS.methods_by_name['DeleteOperation']._options = None
  _OPERATIONS.methods_by_name['DeleteOperation']._serialized_options = b'\202\323\344\223\002\032*\030/v1/{name=operations/**}'
  _OPERATIONS.methods_by_name['CancelOperation']._options = None
  _OPERATIONS.methods_by_name['CancelOperation']._serialized_options = b'\202\323\344\223\002$\"\037/v1/{name=operations/**}:cancel:\001*'
  _OPERATION._serialized_start=225
  _OPERATION._serialized_end=393
  _GETOPERATIONREQUEST._serialized_start=395
  _GETOPERATIONREQUEST._serialized_end=430
  _LISTOPERATIONSREQUEST._serialized_start=433
  _LISTOPERATIONSREQUEST._serialized_end=580
  _OPERATIONFILTER._serialized_start=583
  _OPERATIONFILTER._serialized_end=895
  _LISTOPERATIONSRESPONSE._serialized_start=897
  _LISTOPERATIONSRESPONSE._serialized_end=989
  _CANCELOPERATIONREQUEST._serialized_start=991
  _CANCELOPERATIONREQUEST._serialized_end=1029
  _DELETEOPERATIONREQUEST._serialized_start=1031
  _DELETEOPERATIONREQUEST._serialized_end=1069
  _OPERATIONS._serialized_start=1072
  _OPERATIONS._serialized_end=1546
# @@protoc_insertion_point(module_scope)