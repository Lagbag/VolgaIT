# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from doc_service.api.proto import account_pb2 as doc__service_dot_api_dot_proto_dot_account__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in doc_service/api/proto/account_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AccountRpcServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ValidateJWT = channel.unary_unary(
            '/AccountRpcService/ValidateJWT',
            request_serializer=doc__service_dot_api_dot_proto_dot_account__pb2.JWTRequest.SerializeToString,
            response_deserializer=doc__service_dot_api_dot_proto_dot_account__pb2.JWTResponse.FromString,
            _registered_method=True)
        self.ValidateUser = channel.unary_unary(
            '/AccountRpcService/ValidateUser',
            request_serializer=doc__service_dot_api_dot_proto_dot_account__pb2.UserRequest.SerializeToString,
            response_deserializer=doc__service_dot_api_dot_proto_dot_account__pb2.UserResponse.FromString,
            _registered_method=True)


class AccountRpcServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ValidateJWT(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccountRpcServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'ValidateJWT': grpc.unary_unary_rpc_method_handler(
            servicer.ValidateJWT,
            request_deserializer=doc__service_dot_api_dot_proto_dot_account__pb2.JWTRequest.FromString,
            response_serializer=doc__service_dot_api_dot_proto_dot_account__pb2.JWTResponse.SerializeToString,
        ),
        'ValidateUser': grpc.unary_unary_rpc_method_handler(
            servicer.ValidateUser,
            request_deserializer=doc__service_dot_api_dot_proto_dot_account__pb2.UserRequest.FromString,
            response_serializer=doc__service_dot_api_dot_proto_dot_account__pb2.UserResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'AccountRpcService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('AccountRpcService', rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class AccountRpcService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ValidateJWT(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/AccountRpcService/ValidateJWT',
            doc__service_dot_api_dot_proto_dot_account__pb2.JWTRequest.SerializeToString,
            doc__service_dot_api_dot_proto_dot_account__pb2.JWTResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ValidateUser(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/AccountRpcService/ValidateUser',
            doc__service_dot_api_dot_proto_dot_account__pb2.UserRequest.SerializeToString,
            doc__service_dot_api_dot_proto_dot_account__pb2.UserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
