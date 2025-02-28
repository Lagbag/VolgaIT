# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: hospital.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'hospital.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0ehospital.proto\"&\n\x0fHospitalRequest\x12\x13\n\x0bhospital_id\x18\x01 \x01(\x05\"6\n\x10HospitalResponse\x12\x13\n\x0bhospital_id\x18\x01 \x01(\x05\x12\r\n\x05valid\x18\x02 \x01(\x08\"5\n\x0bRoomRequest\x12\x13\n\x0bhospital_id\x18\x01 \x01(\x05\x12\x11\n\troom_name\x18\x02 \x01(\t\"E\n\x0cRoomResponse\x12\x13\n\x0bhospital_id\x18\x01 \x01(\x05\x12\x11\n\troom_name\x18\x02 \x01(\t\x12\r\n\x05valid\x18\x03 \x01(\x08\"-\n\x16HospitalDeletedRequest\x12\x13\n\x0bhospital_id\x18\x01 \x01(\x05\".\n\x17HospitalDeletedResponse\x12\x13\n\x0bhospital_id\x18\x01 \x01(\x05\x32\xc0\x01\n\x12HospitalRpcService\x12\x37\n\x10ValidateHospital\x12\x10.HospitalRequest\x1a\x11.HospitalResponse\x12+\n\x0cValidateRoom\x12\x0c.RoomRequest\x1a\r.RoomResponse\x12\x44\n\x0fHospitalDeleted\x12\x17.HospitalDeletedRequest\x1a\x18.HospitalDeletedResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hospital_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_HOSPITALREQUEST']._serialized_start = 18
    _globals['_HOSPITALREQUEST']._serialized_end = 56
    _globals['_HOSPITALRESPONSE']._serialized_start = 58
    _globals['_HOSPITALRESPONSE']._serialized_end = 112
    _globals['_ROOMREQUEST']._serialized_start = 114
    _globals['_ROOMREQUEST']._serialized_end = 167
    _globals['_ROOMRESPONSE']._serialized_start = 169
    _globals['_ROOMRESPONSE']._serialized_end = 238
    _globals['_HOSPITALDELETEDREQUEST']._serialized_start = 240
    _globals['_HOSPITALDELETEDREQUEST']._serialized_end = 285
    _globals['_HOSPITALDELETEDRESPONSE']._serialized_start = 287
    _globals['_HOSPITALDELETEDRESPONSE']._serialized_end = 333
    _globals['_HOSPITALRPCSERVICE']._serialized_start = 336
    _globals['_HOSPITALRPCSERVICE']._serialized_end = 528
# @@protoc_insertion_point(module_scope)
