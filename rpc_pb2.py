# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import kv_pb2 as kv__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rpc.proto',
  package='etcdserverpb',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\trpc.proto\x12\x0c\x65tcdserverpb\x1a\x08kv.proto\"\\\n\x0eResponseHeader\x12\x12\n\ncluster_id\x18\x01 \x01(\x04\x12\x11\n\tmember_id\x18\x02 \x01(\x04\x12\x10\n\x08revision\x18\x03 \x01(\x03\x12\x11\n\traft_term\x18\x04 \x01(\x04\"\xe4\x03\n\x0cRangeRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x11\n\trange_end\x18\x02 \x01(\x0c\x12\r\n\x05limit\x18\x03 \x01(\x03\x12\x10\n\x08revision\x18\x04 \x01(\x03\x12\x38\n\nsort_order\x18\x05 \x01(\x0e\x32$.etcdserverpb.RangeRequest.SortOrder\x12:\n\x0bsort_target\x18\x06 \x01(\x0e\x32%.etcdserverpb.RangeRequest.SortTarget\x12\x14\n\x0cserializable\x18\x07 \x01(\x08\x12\x11\n\tkeys_only\x18\x08 \x01(\x08\x12\x12\n\ncount_only\x18\t \x01(\x08\x12\x18\n\x10min_mod_revision\x18\n \x01(\x03\x12\x18\n\x10max_mod_revision\x18\x0b \x01(\x03\x12\x1b\n\x13min_create_revision\x18\x0c \x01(\x03\x12\x1b\n\x13max_create_revision\x18\r \x01(\x03\".\n\tSortOrder\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06\x41SCEND\x10\x01\x12\x0b\n\x07\x44\x45SCEND\x10\x02\"B\n\nSortTarget\x12\x07\n\x03KEY\x10\x00\x12\x0b\n\x07VERSION\x10\x01\x12\n\n\x06\x43REATE\x10\x02\x12\x07\n\x03MOD\x10\x03\x12\t\n\x05VALUE\x10\x04\"y\n\rRangeResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\x1d\n\x03kvs\x18\x02 \x03(\x0b\x32\x10.mvccpb.KeyValue\x12\x0c\n\x04more\x18\x03 \x01(\x08\x12\r\n\x05\x63ount\x18\x04 \x01(\x03\"t\n\nPutRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\r\n\x05lease\x18\x03 \x01(\x03\x12\x0f\n\x07prev_kv\x18\x04 \x01(\x08\x12\x14\n\x0cignore_value\x18\x05 \x01(\x08\x12\x14\n\x0cignore_lease\x18\x06 \x01(\x08\"^\n\x0bPutResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12!\n\x07prev_kv\x18\x02 \x01(\x0b\x32\x10.mvccpb.KeyValue\"E\n\x12\x44\x65leteRangeRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\x11\n\trange_end\x18\x02 \x01(\x0c\x12\x0f\n\x07prev_kv\x18\x03 \x01(\x08\"x\n\x13\x44\x65leteRangeResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\x0f\n\x07\x64\x65leted\x18\x02 \x01(\x03\x12\"\n\x08prev_kvs\x18\x03 \x03(\x0b\x32\x10.mvccpb.KeyValue2\xdc\x01\n\x02KV\x12\x42\n\x05Range\x12\x1a.etcdserverpb.RangeRequest\x1a\x1b.etcdserverpb.RangeResponse\"\x00\x12<\n\x03Put\x12\x18.etcdserverpb.PutRequest\x1a\x19.etcdserverpb.PutResponse\"\x00\x12T\n\x0b\x44\x65leteRange\x12 .etcdserverpb.DeleteRangeRequest\x1a!.etcdserverpb.DeleteRangeResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[kv__pb2.DESCRIPTOR,])



_RANGEREQUEST_SORTORDER = _descriptor.EnumDescriptor(
  name='SortOrder',
  full_name='etcdserverpb.RangeRequest.SortOrder',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ASCEND', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DESCEND', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=502,
  serialized_end=548,
)
_sym_db.RegisterEnumDescriptor(_RANGEREQUEST_SORTORDER)

_RANGEREQUEST_SORTTARGET = _descriptor.EnumDescriptor(
  name='SortTarget',
  full_name='etcdserverpb.RangeRequest.SortTarget',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KEY', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VERSION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CREATE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MOD', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VALUE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=550,
  serialized_end=616,
)
_sym_db.RegisterEnumDescriptor(_RANGEREQUEST_SORTTARGET)


_RESPONSEHEADER = _descriptor.Descriptor(
  name='ResponseHeader',
  full_name='etcdserverpb.ResponseHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='etcdserverpb.ResponseHeader.cluster_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='member_id', full_name='etcdserverpb.ResponseHeader.member_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision', full_name='etcdserverpb.ResponseHeader.revision', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='raft_term', full_name='etcdserverpb.ResponseHeader.raft_term', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=37,
  serialized_end=129,
)


_RANGEREQUEST = _descriptor.Descriptor(
  name='RangeRequest',
  full_name='etcdserverpb.RangeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='etcdserverpb.RangeRequest.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='range_end', full_name='etcdserverpb.RangeRequest.range_end', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='etcdserverpb.RangeRequest.limit', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision', full_name='etcdserverpb.RangeRequest.revision', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sort_order', full_name='etcdserverpb.RangeRequest.sort_order', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sort_target', full_name='etcdserverpb.RangeRequest.sort_target', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serializable', full_name='etcdserverpb.RangeRequest.serializable', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keys_only', full_name='etcdserverpb.RangeRequest.keys_only', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count_only', full_name='etcdserverpb.RangeRequest.count_only', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_mod_revision', full_name='etcdserverpb.RangeRequest.min_mod_revision', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_mod_revision', full_name='etcdserverpb.RangeRequest.max_mod_revision', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_create_revision', full_name='etcdserverpb.RangeRequest.min_create_revision', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_create_revision', full_name='etcdserverpb.RangeRequest.max_create_revision', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RANGEREQUEST_SORTORDER,
    _RANGEREQUEST_SORTTARGET,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=616,
)


_RANGERESPONSE = _descriptor.Descriptor(
  name='RangeResponse',
  full_name='etcdserverpb.RangeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='etcdserverpb.RangeResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kvs', full_name='etcdserverpb.RangeResponse.kvs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='more', full_name='etcdserverpb.RangeResponse.more', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='etcdserverpb.RangeResponse.count', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=618,
  serialized_end=739,
)


_PUTREQUEST = _descriptor.Descriptor(
  name='PutRequest',
  full_name='etcdserverpb.PutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='etcdserverpb.PutRequest.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='etcdserverpb.PutRequest.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lease', full_name='etcdserverpb.PutRequest.lease', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prev_kv', full_name='etcdserverpb.PutRequest.prev_kv', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ignore_value', full_name='etcdserverpb.PutRequest.ignore_value', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ignore_lease', full_name='etcdserverpb.PutRequest.ignore_lease', index=5,
      number=6, type=8, cpp_type=7, label=1,
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
  serialized_start=741,
  serialized_end=857,
)


_PUTRESPONSE = _descriptor.Descriptor(
  name='PutResponse',
  full_name='etcdserverpb.PutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='etcdserverpb.PutResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prev_kv', full_name='etcdserverpb.PutResponse.prev_kv', index=1,
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
  serialized_start=859,
  serialized_end=953,
)


_DELETERANGEREQUEST = _descriptor.Descriptor(
  name='DeleteRangeRequest',
  full_name='etcdserverpb.DeleteRangeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='etcdserverpb.DeleteRangeRequest.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='range_end', full_name='etcdserverpb.DeleteRangeRequest.range_end', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prev_kv', full_name='etcdserverpb.DeleteRangeRequest.prev_kv', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=955,
  serialized_end=1024,
)


_DELETERANGERESPONSE = _descriptor.Descriptor(
  name='DeleteRangeResponse',
  full_name='etcdserverpb.DeleteRangeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='etcdserverpb.DeleteRangeResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='etcdserverpb.DeleteRangeResponse.deleted', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prev_kvs', full_name='etcdserverpb.DeleteRangeResponse.prev_kvs', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=1026,
  serialized_end=1146,
)

_RANGEREQUEST.fields_by_name['sort_order'].enum_type = _RANGEREQUEST_SORTORDER
_RANGEREQUEST.fields_by_name['sort_target'].enum_type = _RANGEREQUEST_SORTTARGET
_RANGEREQUEST_SORTORDER.containing_type = _RANGEREQUEST
_RANGEREQUEST_SORTTARGET.containing_type = _RANGEREQUEST
_RANGERESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
_RANGERESPONSE.fields_by_name['kvs'].message_type = kv__pb2._KEYVALUE
_PUTRESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
_PUTRESPONSE.fields_by_name['prev_kv'].message_type = kv__pb2._KEYVALUE
_DELETERANGERESPONSE.fields_by_name['header'].message_type = _RESPONSEHEADER
_DELETERANGERESPONSE.fields_by_name['prev_kvs'].message_type = kv__pb2._KEYVALUE
DESCRIPTOR.message_types_by_name['ResponseHeader'] = _RESPONSEHEADER
DESCRIPTOR.message_types_by_name['RangeRequest'] = _RANGEREQUEST
DESCRIPTOR.message_types_by_name['RangeResponse'] = _RANGERESPONSE
DESCRIPTOR.message_types_by_name['PutRequest'] = _PUTREQUEST
DESCRIPTOR.message_types_by_name['PutResponse'] = _PUTRESPONSE
DESCRIPTOR.message_types_by_name['DeleteRangeRequest'] = _DELETERANGEREQUEST
DESCRIPTOR.message_types_by_name['DeleteRangeResponse'] = _DELETERANGERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseHeader = _reflection.GeneratedProtocolMessageType('ResponseHeader', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEHEADER,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:etcdserverpb.ResponseHeader)
  })
_sym_db.RegisterMessage(ResponseHeader)

RangeRequest = _reflection.GeneratedProtocolMessageType('RangeRequest', (_message.Message,), {
  'DESCRIPTOR' : _RANGEREQUEST,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:etcdserverpb.RangeRequest)
  })
_sym_db.RegisterMessage(RangeRequest)

RangeResponse = _reflection.GeneratedProtocolMessageType('RangeResponse', (_message.Message,), {
  'DESCRIPTOR' : _RANGERESPONSE,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:etcdserverpb.RangeResponse)
  })
_sym_db.RegisterMessage(RangeResponse)

PutRequest = _reflection.GeneratedProtocolMessageType('PutRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUTREQUEST,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:etcdserverpb.PutRequest)
  })
_sym_db.RegisterMessage(PutRequest)

PutResponse = _reflection.GeneratedProtocolMessageType('PutResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUTRESPONSE,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:etcdserverpb.PutResponse)
  })
_sym_db.RegisterMessage(PutResponse)

DeleteRangeRequest = _reflection.GeneratedProtocolMessageType('DeleteRangeRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETERANGEREQUEST,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:etcdserverpb.DeleteRangeRequest)
  })
_sym_db.RegisterMessage(DeleteRangeRequest)

DeleteRangeResponse = _reflection.GeneratedProtocolMessageType('DeleteRangeResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETERANGERESPONSE,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:etcdserverpb.DeleteRangeResponse)
  })
_sym_db.RegisterMessage(DeleteRangeResponse)



_KV = _descriptor.ServiceDescriptor(
  name='KV',
  full_name='etcdserverpb.KV',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1149,
  serialized_end=1369,
  methods=[
  _descriptor.MethodDescriptor(
    name='Range',
    full_name='etcdserverpb.KV.Range',
    index=0,
    containing_service=None,
    input_type=_RANGEREQUEST,
    output_type=_RANGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Put',
    full_name='etcdserverpb.KV.Put',
    index=1,
    containing_service=None,
    input_type=_PUTREQUEST,
    output_type=_PUTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteRange',
    full_name='etcdserverpb.KV.DeleteRange',
    index=2,
    containing_service=None,
    input_type=_DELETERANGEREQUEST,
    output_type=_DELETERANGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_KV)

DESCRIPTOR.services_by_name['KV'] = _KV

# @@protoc_insertion_point(module_scope)