# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gateway.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from biostarPython.service import cert_pb2 as cert__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gateway.proto',
  package='gateway',
  syntax='proto3',
  serialized_options=_b('\n\032com.supremainc.sdk.gatewayP\001Z\027biostar/service/gateway'),
  serialized_pb=_b('\n\rgateway.proto\x12\x07gateway\x1a\ncert.proto\"H\n\x0bGatewayInfo\x12\x11\n\tgatewayID\x18\x01 \x01(\t\x12\x11\n\tdeviceIDs\x18\x02 \x03(\r\x12\x13\n\x0bisConnected\x18\x03 \x01(\x08\"\x10\n\x0eGetListRequest\"%\n\x0fGetListResponse\x12\x12\n\ngatewayIDs\x18\x01 \x03(\t\" \n\nGetRequest\x12\x12\n\ngatewayIDs\x18\x01 \x03(\t\"9\n\x0bGetResponse\x12*\n\x0cgatewayInfos\x18\x01 \x03(\x0b\x32\x14.gateway.GatewayInfo\" \n\nAddRequest\x12\x12\n\ngatewayIDs\x18\x01 \x03(\t\"\r\n\x0b\x41\x64\x64Response\"#\n\rDeleteRequest\x12\x12\n\ngatewayIDs\x18\x01 \x03(\t\"\x10\n\x0e\x44\x65leteResponse\"g\n\x18\x43reateCertificateRequest\x12\x11\n\tgatewayID\x18\x01 \x01(\t\x12\x1e\n\x07subject\x18\x02 \x01(\x0b\x32\r.cert.PKIName\x12\x18\n\x10\x65xpireAfterYears\x18\x03 \x01(\x05\"D\n\x19\x43reateCertificateResponse\x12\x13\n\x0bgatewayCert\x18\x01 \x01(\t\x12\x12\n\ngatewayKey\x18\x02 \x01(\t\"/\n\x19GetIssuanceHistoryRequest\x12\x12\n\ngatewayIDs\x18\x01 \x03(\t\"\x92\x01\n\x0f\x43\x65rtificateInfo\x12\x11\n\tgatewayID\x18\x01 \x01(\t\x12\x1e\n\x07subject\x18\x02 \x01(\x0b\x32\r.cert.PKIName\x12\x10\n\x08serialNO\x18\x03 \x01(\x03\x12\x11\n\tissueDate\x18\x04 \x01(\x03\x12\x12\n\nexpiryDate\x18\x05 \x01(\x03\x12\x13\n\x0b\x62lacklisted\x18\x06 \x01(\x08\"I\n\x1aGetIssuanceHistoryResponse\x12+\n\tcertInfos\x18\x01 \x03(\x0b\x32\x18.gateway.CertificateInfo\"4\n\x1eGetCertificateBlacklistRequest\x12\x12\n\ngatewayIDs\x18\x01 \x03(\t\"N\n\x1fGetCertificateBlacklistResponse\x12+\n\tcertInfos\x18\x01 \x03(\x0b\x32\x18.gateway.CertificateInfo\"F\n\x1e\x41\x64\x64\x43\x65rtificateBlacklistRequest\x12\x11\n\tgatewayID\x18\x01 \x01(\t\x12\x11\n\tserialNOs\x18\x02 \x03(\x03\"!\n\x1f\x41\x64\x64\x43\x65rtificateBlacklistResponse\"I\n!DeleteCertificateBlacklistRequest\x12\x11\n\tgatewayID\x18\x01 \x01(\t\x12\x11\n\tserialNOs\x18\x02 \x03(\x03\"$\n\"DeleteCertificateBlacklistResponse\"+\n\x16SubscribeStatusRequest\x12\x11\n\tqueueSize\x18\x01 \x01(\x05\"U\n\x0cStatusChange\x12\x11\n\tgatewayID\x18\x01 \x01(\t\x12\x1f\n\x06status\x18\x02 \x01(\x0e\x32\x0f.gateway.Status\x12\x11\n\ttimestamp\x18\x03 \x01(\r*)\n\x06Status\x12\x10\n\x0c\x44ISCONNECTED\x10\x00\x12\r\n\tCONNECTED\x10\x01\x32\xc1\x06\n\x07Gateway\x12<\n\x07GetList\x12\x17.gateway.GetListRequest\x1a\x18.gateway.GetListResponse\x12\x30\n\x03Get\x12\x13.gateway.GetRequest\x1a\x14.gateway.GetResponse\x12\x30\n\x03\x41\x64\x64\x12\x13.gateway.AddRequest\x1a\x14.gateway.AddResponse\x12\x39\n\x06\x44\x65lete\x12\x16.gateway.DeleteRequest\x1a\x17.gateway.DeleteResponse\x12Z\n\x11\x43reateCertificate\x12!.gateway.CreateCertificateRequest\x1a\".gateway.CreateCertificateResponse\x12]\n\x12GetIssuanceHistory\x12\".gateway.GetIssuanceHistoryRequest\x1a#.gateway.GetIssuanceHistoryResponse\x12l\n\x17GetCertificateBlacklist\x12\'.gateway.GetCertificateBlacklistRequest\x1a(.gateway.GetCertificateBlacklistResponse\x12l\n\x17\x41\x64\x64\x43\x65rtificateBlacklist\x12\'.gateway.AddCertificateBlacklistRequest\x1a(.gateway.AddCertificateBlacklistResponse\x12u\n\x1a\x44\x65leteCertificateBlacklist\x12*.gateway.DeleteCertificateBlacklistRequest\x1a+.gateway.DeleteCertificateBlacklistResponse\x12K\n\x0fSubscribeStatus\x12\x1f.gateway.SubscribeStatusRequest\x1a\x15.gateway.StatusChange0\x01\x42\x37\n\x1a\x63om.supremainc.sdk.gatewayP\x01Z\x17\x62iostar/service/gatewayb\x06proto3')
  ,
  dependencies=[cert__pb2.DESCRIPTOR,])

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='gateway.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DISCONNECTED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECTED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1300,
  serialized_end=1341,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
DISCONNECTED = 0
CONNECTED = 1



_GATEWAYINFO = _descriptor.Descriptor(
  name='GatewayInfo',
  full_name='gateway.GatewayInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gatewayID', full_name='gateway.GatewayInfo.gatewayID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceIDs', full_name='gateway.GatewayInfo.deviceIDs', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isConnected', full_name='gateway.GatewayInfo.isConnected', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=38,
  serialized_end=110,
)


_GETLISTREQUEST = _descriptor.Descriptor(
  name='GetListRequest',
  full_name='gateway.GetListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=112,
  serialized_end=128,
)


_GETLISTRESPONSE = _descriptor.Descriptor(
  name='GetListResponse',
  full_name='gateway.GetListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gatewayIDs', full_name='gateway.GetListResponse.gatewayIDs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=130,
  serialized_end=167,
)


_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='gateway.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gatewayIDs', full_name='gateway.GetRequest.gatewayIDs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=169,
  serialized_end=201,
)


_GETRESPONSE = _descriptor.Descriptor(
  name='GetResponse',
  full_name='gateway.GetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gatewayInfos', full_name='gateway.GetResponse.gatewayInfos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=203,
  serialized_end=260,
)


_ADDREQUEST = _descriptor.Descriptor(
  name='AddRequest',
  full_name='gateway.AddRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gatewayIDs', full_name='gateway.AddRequest.gatewayIDs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=262,
  serialized_end=294,
)


_ADDRESPONSE = _descriptor.Descriptor(
  name='AddResponse',
  full_name='gateway.AddResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=296,
  serialized_end=309,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='gateway.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gatewayIDs', full_name='gateway.DeleteRequest.gatewayIDs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=311,
  serialized_end=346,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='gateway.DeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=348,
  serialized_end=364,
)


_CREATECERTIFICATEREQUEST = _descriptor.Descriptor(
  name='CreateCertificateRequest',
  full_name='gateway.CreateCertificateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gatewayID', full_name='gateway.CreateCertificateRequest.gatewayID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subject', full_name='gateway.CreateCertificateRequest.subject', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expireAfterYears', full_name='gateway.CreateCertificateRequest.expireAfterYears', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=366,
  serialized_end=469,
)


_CREATECERTIFICATERESPONSE = _descriptor.Descriptor(
  name='CreateCertificateResponse',
  full_name='gateway.CreateCertificateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gatewayCert', full_name='gateway.CreateCertificateResponse.gatewayCert', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gatewayKey', full_name='gateway.CreateCertificateResponse.gatewayKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=471,
  serialized_end=539,
)


_GETISSUANCEHISTORYREQUEST = _descriptor.Descriptor(
  name='GetIssuanceHistoryRequest',
  full_name='gateway.GetIssuanceHistoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gatewayIDs', full_name='gateway.GetIssuanceHistoryRequest.gatewayIDs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=541,
  serialized_end=588,
)


_CERTIFICATEINFO = _descriptor.Descriptor(
  name='CertificateInfo',
  full_name='gateway.CertificateInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gatewayID', full_name='gateway.CertificateInfo.gatewayID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subject', full_name='gateway.CertificateInfo.subject', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialNO', full_name='gateway.CertificateInfo.serialNO', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issueDate', full_name='gateway.CertificateInfo.issueDate', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiryDate', full_name='gateway.CertificateInfo.expiryDate', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blacklisted', full_name='gateway.CertificateInfo.blacklisted', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=591,
  serialized_end=737,
)


_GETISSUANCEHISTORYRESPONSE = _descriptor.Descriptor(
  name='GetIssuanceHistoryResponse',
  full_name='gateway.GetIssuanceHistoryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='certInfos', full_name='gateway.GetIssuanceHistoryResponse.certInfos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=739,
  serialized_end=812,
)


_GETCERTIFICATEBLACKLISTREQUEST = _descriptor.Descriptor(
  name='GetCertificateBlacklistRequest',
  full_name='gateway.GetCertificateBlacklistRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gatewayIDs', full_name='gateway.GetCertificateBlacklistRequest.gatewayIDs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=814,
  serialized_end=866,
)


_GETCERTIFICATEBLACKLISTRESPONSE = _descriptor.Descriptor(
  name='GetCertificateBlacklistResponse',
  full_name='gateway.GetCertificateBlacklistResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='certInfos', full_name='gateway.GetCertificateBlacklistResponse.certInfos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=868,
  serialized_end=946,
)


_ADDCERTIFICATEBLACKLISTREQUEST = _descriptor.Descriptor(
  name='AddCertificateBlacklistRequest',
  full_name='gateway.AddCertificateBlacklistRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gatewayID', full_name='gateway.AddCertificateBlacklistRequest.gatewayID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialNOs', full_name='gateway.AddCertificateBlacklistRequest.serialNOs', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=948,
  serialized_end=1018,
)


_ADDCERTIFICATEBLACKLISTRESPONSE = _descriptor.Descriptor(
  name='AddCertificateBlacklistResponse',
  full_name='gateway.AddCertificateBlacklistResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1020,
  serialized_end=1053,
)


_DELETECERTIFICATEBLACKLISTREQUEST = _descriptor.Descriptor(
  name='DeleteCertificateBlacklistRequest',
  full_name='gateway.DeleteCertificateBlacklistRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gatewayID', full_name='gateway.DeleteCertificateBlacklistRequest.gatewayID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialNOs', full_name='gateway.DeleteCertificateBlacklistRequest.serialNOs', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1055,
  serialized_end=1128,
)


_DELETECERTIFICATEBLACKLISTRESPONSE = _descriptor.Descriptor(
  name='DeleteCertificateBlacklistResponse',
  full_name='gateway.DeleteCertificateBlacklistResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1130,
  serialized_end=1166,
)


_SUBSCRIBESTATUSREQUEST = _descriptor.Descriptor(
  name='SubscribeStatusRequest',
  full_name='gateway.SubscribeStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queueSize', full_name='gateway.SubscribeStatusRequest.queueSize', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1168,
  serialized_end=1211,
)


_STATUSCHANGE = _descriptor.Descriptor(
  name='StatusChange',
  full_name='gateway.StatusChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gatewayID', full_name='gateway.StatusChange.gatewayID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='gateway.StatusChange.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='gateway.StatusChange.timestamp', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1213,
  serialized_end=1298,
)

_GETRESPONSE.fields_by_name['gatewayInfos'].message_type = _GATEWAYINFO
_CREATECERTIFICATEREQUEST.fields_by_name['subject'].message_type = cert__pb2._PKINAME
_CERTIFICATEINFO.fields_by_name['subject'].message_type = cert__pb2._PKINAME
_GETISSUANCEHISTORYRESPONSE.fields_by_name['certInfos'].message_type = _CERTIFICATEINFO
_GETCERTIFICATEBLACKLISTRESPONSE.fields_by_name['certInfos'].message_type = _CERTIFICATEINFO
_STATUSCHANGE.fields_by_name['status'].enum_type = _STATUS
DESCRIPTOR.message_types_by_name['GatewayInfo'] = _GATEWAYINFO
DESCRIPTOR.message_types_by_name['GetListRequest'] = _GETLISTREQUEST
DESCRIPTOR.message_types_by_name['GetListResponse'] = _GETLISTRESPONSE
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['GetResponse'] = _GETRESPONSE
DESCRIPTOR.message_types_by_name['AddRequest'] = _ADDREQUEST
DESCRIPTOR.message_types_by_name['AddResponse'] = _ADDRESPONSE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
DESCRIPTOR.message_types_by_name['CreateCertificateRequest'] = _CREATECERTIFICATEREQUEST
DESCRIPTOR.message_types_by_name['CreateCertificateResponse'] = _CREATECERTIFICATERESPONSE
DESCRIPTOR.message_types_by_name['GetIssuanceHistoryRequest'] = _GETISSUANCEHISTORYREQUEST
DESCRIPTOR.message_types_by_name['CertificateInfo'] = _CERTIFICATEINFO
DESCRIPTOR.message_types_by_name['GetIssuanceHistoryResponse'] = _GETISSUANCEHISTORYRESPONSE
DESCRIPTOR.message_types_by_name['GetCertificateBlacklistRequest'] = _GETCERTIFICATEBLACKLISTREQUEST
DESCRIPTOR.message_types_by_name['GetCertificateBlacklistResponse'] = _GETCERTIFICATEBLACKLISTRESPONSE
DESCRIPTOR.message_types_by_name['AddCertificateBlacklistRequest'] = _ADDCERTIFICATEBLACKLISTREQUEST
DESCRIPTOR.message_types_by_name['AddCertificateBlacklistResponse'] = _ADDCERTIFICATEBLACKLISTRESPONSE
DESCRIPTOR.message_types_by_name['DeleteCertificateBlacklistRequest'] = _DELETECERTIFICATEBLACKLISTREQUEST
DESCRIPTOR.message_types_by_name['DeleteCertificateBlacklistResponse'] = _DELETECERTIFICATEBLACKLISTRESPONSE
DESCRIPTOR.message_types_by_name['SubscribeStatusRequest'] = _SUBSCRIBESTATUSREQUEST
DESCRIPTOR.message_types_by_name['StatusChange'] = _STATUSCHANGE
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GatewayInfo = _reflection.GeneratedProtocolMessageType('GatewayInfo', (_message.Message,), dict(
  DESCRIPTOR = _GATEWAYINFO,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GatewayInfo)
  ))
_sym_db.RegisterMessage(GatewayInfo)

GetListRequest = _reflection.GeneratedProtocolMessageType('GetListRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETLISTREQUEST,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetListRequest)
  ))
_sym_db.RegisterMessage(GetListRequest)

GetListResponse = _reflection.GeneratedProtocolMessageType('GetListResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETLISTRESPONSE,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetListResponse)
  ))
_sym_db.RegisterMessage(GetListResponse)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREQUEST,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetRequest)
  ))
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETRESPONSE,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetResponse)
  ))
_sym_db.RegisterMessage(GetResponse)

AddRequest = _reflection.GeneratedProtocolMessageType('AddRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDREQUEST,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.AddRequest)
  ))
_sym_db.RegisterMessage(AddRequest)

AddResponse = _reflection.GeneratedProtocolMessageType('AddResponse', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESPONSE,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.AddResponse)
  ))
_sym_db.RegisterMessage(AddResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEREQUEST,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.DeleteRequest)
  ))
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETERESPONSE,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.DeleteResponse)
  ))
_sym_db.RegisterMessage(DeleteResponse)

CreateCertificateRequest = _reflection.GeneratedProtocolMessageType('CreateCertificateRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATECERTIFICATEREQUEST,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.CreateCertificateRequest)
  ))
_sym_db.RegisterMessage(CreateCertificateRequest)

CreateCertificateResponse = _reflection.GeneratedProtocolMessageType('CreateCertificateResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATECERTIFICATERESPONSE,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.CreateCertificateResponse)
  ))
_sym_db.RegisterMessage(CreateCertificateResponse)

GetIssuanceHistoryRequest = _reflection.GeneratedProtocolMessageType('GetIssuanceHistoryRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETISSUANCEHISTORYREQUEST,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetIssuanceHistoryRequest)
  ))
_sym_db.RegisterMessage(GetIssuanceHistoryRequest)

CertificateInfo = _reflection.GeneratedProtocolMessageType('CertificateInfo', (_message.Message,), dict(
  DESCRIPTOR = _CERTIFICATEINFO,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.CertificateInfo)
  ))
_sym_db.RegisterMessage(CertificateInfo)

GetIssuanceHistoryResponse = _reflection.GeneratedProtocolMessageType('GetIssuanceHistoryResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETISSUANCEHISTORYRESPONSE,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetIssuanceHistoryResponse)
  ))
_sym_db.RegisterMessage(GetIssuanceHistoryResponse)

GetCertificateBlacklistRequest = _reflection.GeneratedProtocolMessageType('GetCertificateBlacklistRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCERTIFICATEBLACKLISTREQUEST,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetCertificateBlacklistRequest)
  ))
_sym_db.RegisterMessage(GetCertificateBlacklistRequest)

GetCertificateBlacklistResponse = _reflection.GeneratedProtocolMessageType('GetCertificateBlacklistResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETCERTIFICATEBLACKLISTRESPONSE,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetCertificateBlacklistResponse)
  ))
_sym_db.RegisterMessage(GetCertificateBlacklistResponse)

AddCertificateBlacklistRequest = _reflection.GeneratedProtocolMessageType('AddCertificateBlacklistRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDCERTIFICATEBLACKLISTREQUEST,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.AddCertificateBlacklistRequest)
  ))
_sym_db.RegisterMessage(AddCertificateBlacklistRequest)

AddCertificateBlacklistResponse = _reflection.GeneratedProtocolMessageType('AddCertificateBlacklistResponse', (_message.Message,), dict(
  DESCRIPTOR = _ADDCERTIFICATEBLACKLISTRESPONSE,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.AddCertificateBlacklistResponse)
  ))
_sym_db.RegisterMessage(AddCertificateBlacklistResponse)

DeleteCertificateBlacklistRequest = _reflection.GeneratedProtocolMessageType('DeleteCertificateBlacklistRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETECERTIFICATEBLACKLISTREQUEST,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.DeleteCertificateBlacklistRequest)
  ))
_sym_db.RegisterMessage(DeleteCertificateBlacklistRequest)

DeleteCertificateBlacklistResponse = _reflection.GeneratedProtocolMessageType('DeleteCertificateBlacklistResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETECERTIFICATEBLACKLISTRESPONSE,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.DeleteCertificateBlacklistResponse)
  ))
_sym_db.RegisterMessage(DeleteCertificateBlacklistResponse)

SubscribeStatusRequest = _reflection.GeneratedProtocolMessageType('SubscribeStatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBESTATUSREQUEST,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.SubscribeStatusRequest)
  ))
_sym_db.RegisterMessage(SubscribeStatusRequest)

StatusChange = _reflection.GeneratedProtocolMessageType('StatusChange', (_message.Message,), dict(
  DESCRIPTOR = _STATUSCHANGE,
  __module__ = 'gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.StatusChange)
  ))
_sym_db.RegisterMessage(StatusChange)


DESCRIPTOR._options = None

_GATEWAY = _descriptor.ServiceDescriptor(
  name='Gateway',
  full_name='gateway.Gateway',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1344,
  serialized_end=2177,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetList',
    full_name='gateway.Gateway.GetList',
    index=0,
    containing_service=None,
    input_type=_GETLISTREQUEST,
    output_type=_GETLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='gateway.Gateway.Get',
    index=1,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_GETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Add',
    full_name='gateway.Gateway.Add',
    index=2,
    containing_service=None,
    input_type=_ADDREQUEST,
    output_type=_ADDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='gateway.Gateway.Delete',
    index=3,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateCertificate',
    full_name='gateway.Gateway.CreateCertificate',
    index=4,
    containing_service=None,
    input_type=_CREATECERTIFICATEREQUEST,
    output_type=_CREATECERTIFICATERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetIssuanceHistory',
    full_name='gateway.Gateway.GetIssuanceHistory',
    index=5,
    containing_service=None,
    input_type=_GETISSUANCEHISTORYREQUEST,
    output_type=_GETISSUANCEHISTORYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetCertificateBlacklist',
    full_name='gateway.Gateway.GetCertificateBlacklist',
    index=6,
    containing_service=None,
    input_type=_GETCERTIFICATEBLACKLISTREQUEST,
    output_type=_GETCERTIFICATEBLACKLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddCertificateBlacklist',
    full_name='gateway.Gateway.AddCertificateBlacklist',
    index=7,
    containing_service=None,
    input_type=_ADDCERTIFICATEBLACKLISTREQUEST,
    output_type=_ADDCERTIFICATEBLACKLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteCertificateBlacklist',
    full_name='gateway.Gateway.DeleteCertificateBlacklist',
    index=8,
    containing_service=None,
    input_type=_DELETECERTIFICATEBLACKLISTREQUEST,
    output_type=_DELETECERTIFICATEBLACKLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeStatus',
    full_name='gateway.Gateway.SubscribeStatus',
    index=9,
    containing_service=None,
    input_type=_SUBSCRIBESTATUSREQUEST,
    output_type=_STATUSCHANGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GATEWAY)

DESCRIPTOR.services_by_name['Gateway'] = _GATEWAY

# @@protoc_insertion_point(module_scope)
