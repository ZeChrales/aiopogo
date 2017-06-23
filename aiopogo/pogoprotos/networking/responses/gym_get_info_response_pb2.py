# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/gym_get_info_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.gym import gym_status_and_defenders_pb2 as pogoprotos_dot_data_dot_gym_dot_gym__status__and__defenders__pb2
from pogoprotos.data.badge import awarded_gym_badge_pb2 as pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/gym_get_info_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n;pogoprotos/networking/responses/gym_get_info_response.proto\x12\x1fpogoprotos.networking.responses\x1a\x32pogoprotos/data/gym/gym_status_and_defenders.proto\x1a-pogoprotos/data/badge/awarded_gym_badge.proto\"\xa5\x03\n\x12GymGetInfoResponse\x12L\n\x18gym_status_and_defenders\x18\x01 \x01(\x0b\x32*.pogoprotos.data.gym.GymStatusAndDefenders\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12J\n\x06result\x18\x04 \x01(\x0e\x32:.pogoprotos.networking.responses.GymGetInfoResponse.Result\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x15\n\rsecondary_url\x18\x06 \x01(\t\x12\x41\n\x11\x61warded_gym_badge\x18\x07 \x01(\x0b\x32&.pogoprotos.data.badge.AwardedGymBadge\x12\x19\n\x11\x63heckin_image_url\x18\x08 \x01(\t\"P\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x16\n\x12\x45RROR_NOT_IN_RANGE\x10\x02\x12\x16\n\x12\x45RROR_GYM_DISABLED\x10\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_gym_dot_gym__status__and__defenders__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2.DESCRIPTOR,])



_GYMGETINFORESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GymGetInfoResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_IN_RANGE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_GYM_DISABLED', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=537,
  serialized_end=617,
)
_sym_db.RegisterEnumDescriptor(_GYMGETINFORESPONSE_RESULT)


_GYMGETINFORESPONSE = _descriptor.Descriptor(
  name='GymGetInfoResponse',
  full_name='pogoprotos.networking.responses.GymGetInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gym_status_and_defenders', full_name='pogoprotos.networking.responses.GymGetInfoResponse.gym_status_and_defenders', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='pogoprotos.networking.responses.GymGetInfoResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='pogoprotos.networking.responses.GymGetInfoResponse.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GymGetInfoResponse.result', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='pogoprotos.networking.responses.GymGetInfoResponse.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='secondary_url', full_name='pogoprotos.networking.responses.GymGetInfoResponse.secondary_url', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='awarded_gym_badge', full_name='pogoprotos.networking.responses.GymGetInfoResponse.awarded_gym_badge', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checkin_image_url', full_name='pogoprotos.networking.responses.GymGetInfoResponse.checkin_image_url', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GYMGETINFORESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=617,
)

_GYMGETINFORESPONSE.fields_by_name['gym_status_and_defenders'].message_type = pogoprotos_dot_data_dot_gym_dot_gym__status__and__defenders__pb2._GYMSTATUSANDDEFENDERS
_GYMGETINFORESPONSE.fields_by_name['result'].enum_type = _GYMGETINFORESPONSE_RESULT
_GYMGETINFORESPONSE.fields_by_name['awarded_gym_badge'].message_type = pogoprotos_dot_data_dot_badge_dot_awarded__gym__badge__pb2._AWARDEDGYMBADGE
_GYMGETINFORESPONSE_RESULT.containing_type = _GYMGETINFORESPONSE
DESCRIPTOR.message_types_by_name['GymGetInfoResponse'] = _GYMGETINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GymGetInfoResponse = _reflection.GeneratedProtocolMessageType('GymGetInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _GYMGETINFORESPONSE,
  __module__ = 'pogoprotos.networking.responses.gym_get_info_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GymGetInfoResponse)
  ))
_sym_db.RegisterMessage(GymGetInfoResponse)


# @@protoc_insertion_point(module_scope)
