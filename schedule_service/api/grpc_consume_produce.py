import logging

import grpc
from django.conf import settings

from .proto import account_pb2_grpc, hospital_pb2_grpc, account_pb2

GRPC_PORT_ACCOUNT = settings.GRPC_PORT_ACCOUNT
GRPC_PORT_HOSPITAL = settings.GRPC_PORT_HOSPITAL
logger = logging.getLogger(__name__)


def grpc_user_by_jwt(raw_token):
    try:
        channel = grpc.insecure_channel(f"auth_service:{GRPC_PORT_ACCOUNT}")
        client = account_pb2_grpc.AccountRpcServiceStub(channel)
        request = account_pb2.JWTRequest(jwt=raw_token)
        response = client.ValidateJWT(request)
        user = getattr(response, "user", None)
        return user
    except Exception as e:
        logger.error(f"gRPC ERROR WHEN TRYINA CHECK JWT: {e}")
        return


def grpc_check_roles(user_id, role=None):
    try:
        channel = grpc.insecure_channel(f"auth_service:{GRPC_PORT_ACCOUNT}")
        client = account_pb2_grpc.AccountRpcServiceStub(channel)
        request = UserRequest(user_id=user_id, role=role)
        response = client.ValidateUser(request)
        user = getattr(response, "user", None)
        return user, response.valid
    except Exception as e:
        logger.error(f"gRPC ERROR WHEN TRYINA CHECK USER (user_id = {user_id}) (role = {role}): {e}")
        return


def grpc_check_hospital(hospital_id):
    try:
        channel = grpc.insecure_channel(f"health_service:{GRPC_PORT_HOSPITAL}")
        client = hospital_pb2_grpc.HospitalRpcServiceStub(channel)
        request = HospitalRequest(hospital_id=hospital_id)
        response = client.ValidateHospital(request)
        valid = getattr(response, "valid", False)
        return valid
    except Exception as e:
        logger.error(f"gRPC ERROR WHEN TRYINA CHECK HOSPITAL (hospital_id = {hospital_id}): {e}")
        return False


def grpc_check_room(hospital_id, room_name):
    try:
        channel = grpc.insecure_channel(f"health_service:{GRPC_PORT_HOSPITAL}")
        client = hospital_pb2_grpc.HospitalRpcServiceStub(channel)
        request = RoomRequest(hospital_id=hospital_id, room_name=room_name)
        response = client.ValidateRoom(request)
        valid = getattr(response, "valid", False)
        return valid
    except Exception as e:
        logger.error(f"gRPC ERROR WHEN TRYINA CHECK ROOM (hospital_id = {hospital_id}) (room_name = {room_name}): {e}")
        return False
