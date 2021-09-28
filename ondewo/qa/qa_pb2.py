# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ondewo/qa/qa.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ondewo.nlu import session_pb2 as ondewo_dot_nlu_dot_session__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ondewo/qa/qa.proto',
  package='ondewo.qa',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12ondewo/qa/qa.proto\x12\tondewo.qa\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x18ondewo/nlu/session.proto\"\xfb\x01\n\x10GetAnswerRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12#\n\x04text\x18\x02 \x01(\x0b\x32\x15.ondewo.nlu.TextInput\x12\x17\n\x0fmax_num_answers\x18\x03 \x01(\x05\x12\x18\n\x10threshold_reader\x18\x04 \x01(\x02\x12\x1b\n\x13threshold_retriever\x18\x05 \x01(\x02\x12\x19\n\x11threshold_overall\x18\x06 \x01(\x02\x12\x19\n\x11reader_model_name\x18\x07 \x01(\t\x12(\n\nurl_filter\x18\x08 \x01(\x0b\x32\x14.ondewo.qa.UrlFilter\"K\n\x11GetAnswerResponse\x12\x36\n\x0cquery_result\x18\x02 \x01(\x0b\x32 .ondewo.nlu.DetectIntentResponse\"B\n\x12RunScraperResponse\x12\x16\n\x0e\x63ontainer_name\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontainer_id\x18\x02 \x01(\t\"3\n\x13RunTrainingResponse\x12\n\n\x02\x66\x31\x18\x01 \x01(\x02\x12\x10\n\x08\x61\x63\x63uracy\x18\x02 \x01(\x02\"_\n\tUrlFilter\x12\x16\n\x0e\x61llowed_values\x18\x01 \x03(\t\x12\x1c\n\x14regex_filter_include\x18\x02 \x01(\t\x12\x1c\n\x14regex_filter_exclude\x18\x03 \x01(\t\"1\n\x16GetServerStateResponse\x12\x17\n\x0fserver_is_ready\x18\x01 \x01(\x08\"-\n\x16ListProjectIdsResponse\x12\x13\n\x0bproject_ids\x18\x01 \x03(\t\"-\n\x17GetProjectConfigRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\"5\n\x18GetProjectConfigResponse\x12\x19\n\x11\x63onfig_serialized\x18\x01 \x01(\t\",\n\x16UpdateDatabaseResponse\x12\x12\n\nsuccessful\x18\x01 \x01(\x08\x32\xd0\x05\n\x02QA\x12V\n\tGetAnswer\x12\x1b.ondewo.qa.GetAnswerRequest\x1a\x1c.ondewo.qa.GetAnswerResponse\"\x0e\x82\xd3\xe4\x93\x02\x08\"\x03/qa:\x01*\x12[\n\nRunScraper\x12\x16.google.protobuf.Empty\x1a\x1d.ondewo.qa.RunScraperResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/qa:RunScraper\x12g\n\x0eUpdateDatabase\x12\x16.google.protobuf.Empty\x1a!.ondewo.qa.UpdateDatabaseResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/qa:UpdateDatabase\x12^\n\x0bRunTraining\x12\x16.google.protobuf.Empty\x1a\x1e.ondewo.qa.RunTrainingResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/qa:RunTraining\x12g\n\x0eGetServerState\x12\x16.google.protobuf.Empty\x1a!.ondewo.qa.GetServerStateResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/qa:GetServerState\x12g\n\x0eListProjectIds\x12\x16.google.protobuf.Empty\x1a!.ondewo.qa.ListProjectIdsResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/qa:ListProjectIds\x12z\n\x10GetProjectConfig\x12\".ondewo.qa.GetProjectConfigRequest\x1a#.ondewo.qa.GetProjectConfigResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/qa:ListProjectConfigb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,ondewo_dot_nlu_dot_session__pb2.DESCRIPTOR,])




_GETANSWERREQUEST = _descriptor.Descriptor(
  name='GetAnswerRequest',
  full_name='ondewo.qa.GetAnswerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='ondewo.qa.GetAnswerRequest.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='ondewo.qa.GetAnswerRequest.text', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_num_answers', full_name='ondewo.qa.GetAnswerRequest.max_num_answers', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='threshold_reader', full_name='ondewo.qa.GetAnswerRequest.threshold_reader', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='threshold_retriever', full_name='ondewo.qa.GetAnswerRequest.threshold_retriever', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='threshold_overall', full_name='ondewo.qa.GetAnswerRequest.threshold_overall', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reader_model_name', full_name='ondewo.qa.GetAnswerRequest.reader_model_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url_filter', full_name='ondewo.qa.GetAnswerRequest.url_filter', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=370,
)


_GETANSWERRESPONSE = _descriptor.Descriptor(
  name='GetAnswerResponse',
  full_name='ondewo.qa.GetAnswerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_result', full_name='ondewo.qa.GetAnswerResponse.query_result', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=447,
)


_RUNSCRAPERRESPONSE = _descriptor.Descriptor(
  name='RunScraperResponse',
  full_name='ondewo.qa.RunScraperResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='container_name', full_name='ondewo.qa.RunScraperResponse.container_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='container_id', full_name='ondewo.qa.RunScraperResponse.container_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=449,
  serialized_end=515,
)


_RUNTRAININGRESPONSE = _descriptor.Descriptor(
  name='RunTrainingResponse',
  full_name='ondewo.qa.RunTrainingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='f1', full_name='ondewo.qa.RunTrainingResponse.f1', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accuracy', full_name='ondewo.qa.RunTrainingResponse.accuracy', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=517,
  serialized_end=568,
)


_URLFILTER = _descriptor.Descriptor(
  name='UrlFilter',
  full_name='ondewo.qa.UrlFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='allowed_values', full_name='ondewo.qa.UrlFilter.allowed_values', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regex_filter_include', full_name='ondewo.qa.UrlFilter.regex_filter_include', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regex_filter_exclude', full_name='ondewo.qa.UrlFilter.regex_filter_exclude', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=570,
  serialized_end=665,
)


_GETSERVERSTATERESPONSE = _descriptor.Descriptor(
  name='GetServerStateResponse',
  full_name='ondewo.qa.GetServerStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_is_ready', full_name='ondewo.qa.GetServerStateResponse.server_is_ready', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=667,
  serialized_end=716,
)


_LISTPROJECTIDSRESPONSE = _descriptor.Descriptor(
  name='ListProjectIdsResponse',
  full_name='ondewo.qa.ListProjectIdsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_ids', full_name='ondewo.qa.ListProjectIdsResponse.project_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=718,
  serialized_end=763,
)


_GETPROJECTCONFIGREQUEST = _descriptor.Descriptor(
  name='GetProjectConfigRequest',
  full_name='ondewo.qa.GetProjectConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='ondewo.qa.GetProjectConfigRequest.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=765,
  serialized_end=810,
)


_GETPROJECTCONFIGRESPONSE = _descriptor.Descriptor(
  name='GetProjectConfigResponse',
  full_name='ondewo.qa.GetProjectConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='config_serialized', full_name='ondewo.qa.GetProjectConfigResponse.config_serialized', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=812,
  serialized_end=865,
)


_UPDATEDATABASERESPONSE = _descriptor.Descriptor(
  name='UpdateDatabaseResponse',
  full_name='ondewo.qa.UpdateDatabaseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='successful', full_name='ondewo.qa.UpdateDatabaseResponse.successful', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=867,
  serialized_end=911,
)

_GETANSWERREQUEST.fields_by_name['text'].message_type = ondewo_dot_nlu_dot_session__pb2._TEXTINPUT
_GETANSWERREQUEST.fields_by_name['url_filter'].message_type = _URLFILTER
_GETANSWERRESPONSE.fields_by_name['query_result'].message_type = ondewo_dot_nlu_dot_session__pb2._DETECTINTENTRESPONSE
DESCRIPTOR.message_types_by_name['GetAnswerRequest'] = _GETANSWERREQUEST
DESCRIPTOR.message_types_by_name['GetAnswerResponse'] = _GETANSWERRESPONSE
DESCRIPTOR.message_types_by_name['RunScraperResponse'] = _RUNSCRAPERRESPONSE
DESCRIPTOR.message_types_by_name['RunTrainingResponse'] = _RUNTRAININGRESPONSE
DESCRIPTOR.message_types_by_name['UrlFilter'] = _URLFILTER
DESCRIPTOR.message_types_by_name['GetServerStateResponse'] = _GETSERVERSTATERESPONSE
DESCRIPTOR.message_types_by_name['ListProjectIdsResponse'] = _LISTPROJECTIDSRESPONSE
DESCRIPTOR.message_types_by_name['GetProjectConfigRequest'] = _GETPROJECTCONFIGREQUEST
DESCRIPTOR.message_types_by_name['GetProjectConfigResponse'] = _GETPROJECTCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['UpdateDatabaseResponse'] = _UPDATEDATABASERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAnswerRequest = _reflection.GeneratedProtocolMessageType('GetAnswerRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETANSWERREQUEST,
  '__module__' : 'ondewo.qa.qa_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.qa.GetAnswerRequest)
  })
_sym_db.RegisterMessage(GetAnswerRequest)

GetAnswerResponse = _reflection.GeneratedProtocolMessageType('GetAnswerResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETANSWERRESPONSE,
  '__module__' : 'ondewo.qa.qa_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.qa.GetAnswerResponse)
  })
_sym_db.RegisterMessage(GetAnswerResponse)

RunScraperResponse = _reflection.GeneratedProtocolMessageType('RunScraperResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNSCRAPERRESPONSE,
  '__module__' : 'ondewo.qa.qa_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.qa.RunScraperResponse)
  })
_sym_db.RegisterMessage(RunScraperResponse)

RunTrainingResponse = _reflection.GeneratedProtocolMessageType('RunTrainingResponse', (_message.Message,), {
  'DESCRIPTOR' : _RUNTRAININGRESPONSE,
  '__module__' : 'ondewo.qa.qa_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.qa.RunTrainingResponse)
  })
_sym_db.RegisterMessage(RunTrainingResponse)

UrlFilter = _reflection.GeneratedProtocolMessageType('UrlFilter', (_message.Message,), {
  'DESCRIPTOR' : _URLFILTER,
  '__module__' : 'ondewo.qa.qa_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.qa.UrlFilter)
  })
_sym_db.RegisterMessage(UrlFilter)

GetServerStateResponse = _reflection.GeneratedProtocolMessageType('GetServerStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVERSTATERESPONSE,
  '__module__' : 'ondewo.qa.qa_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.qa.GetServerStateResponse)
  })
_sym_db.RegisterMessage(GetServerStateResponse)

ListProjectIdsResponse = _reflection.GeneratedProtocolMessageType('ListProjectIdsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROJECTIDSRESPONSE,
  '__module__' : 'ondewo.qa.qa_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.qa.ListProjectIdsResponse)
  })
_sym_db.RegisterMessage(ListProjectIdsResponse)

GetProjectConfigRequest = _reflection.GeneratedProtocolMessageType('GetProjectConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTCONFIGREQUEST,
  '__module__' : 'ondewo.qa.qa_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.qa.GetProjectConfigRequest)
  })
_sym_db.RegisterMessage(GetProjectConfigRequest)

GetProjectConfigResponse = _reflection.GeneratedProtocolMessageType('GetProjectConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPROJECTCONFIGRESPONSE,
  '__module__' : 'ondewo.qa.qa_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.qa.GetProjectConfigResponse)
  })
_sym_db.RegisterMessage(GetProjectConfigResponse)

UpdateDatabaseResponse = _reflection.GeneratedProtocolMessageType('UpdateDatabaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATABASERESPONSE,
  '__module__' : 'ondewo.qa.qa_pb2'
  # @@protoc_insertion_point(class_scope:ondewo.qa.UpdateDatabaseResponse)
  })
_sym_db.RegisterMessage(UpdateDatabaseResponse)



_QA = _descriptor.ServiceDescriptor(
  name='QA',
  full_name='ondewo.qa.QA',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=914,
  serialized_end=1634,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAnswer',
    full_name='ondewo.qa.QA.GetAnswer',
    index=0,
    containing_service=None,
    input_type=_GETANSWERREQUEST,
    output_type=_GETANSWERRESPONSE,
    serialized_options=b'\202\323\344\223\002\010\"\003/qa:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RunScraper',
    full_name='ondewo.qa.QA.RunScraper',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_RUNSCRAPERRESPONSE,
    serialized_options=b'\202\323\344\223\002\020\022\016/qa:RunScraper',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateDatabase',
    full_name='ondewo.qa.QA.UpdateDatabase',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_UPDATEDATABASERESPONSE,
    serialized_options=b'\202\323\344\223\002\024\022\022/qa:UpdateDatabase',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RunTraining',
    full_name='ondewo.qa.QA.RunTraining',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_RUNTRAININGRESPONSE,
    serialized_options=b'\202\323\344\223\002\021\022\017/qa:RunTraining',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetServerState',
    full_name='ondewo.qa.QA.GetServerState',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_GETSERVERSTATERESPONSE,
    serialized_options=b'\202\323\344\223\002\024\022\022/qa:GetServerState',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListProjectIds',
    full_name='ondewo.qa.QA.ListProjectIds',
    index=5,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_LISTPROJECTIDSRESPONSE,
    serialized_options=b'\202\323\344\223\002\024\022\022/qa:ListProjectIds',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetProjectConfig',
    full_name='ondewo.qa.QA.GetProjectConfig',
    index=6,
    containing_service=None,
    input_type=_GETPROJECTCONFIGREQUEST,
    output_type=_GETPROJECTCONFIGRESPONSE,
    serialized_options=b'\202\323\344\223\002\027\022\025/qa:ListProjectConfig',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QA)

DESCRIPTOR.services_by_name['QA'] = _QA

# @@protoc_insertion_point(module_scope)
