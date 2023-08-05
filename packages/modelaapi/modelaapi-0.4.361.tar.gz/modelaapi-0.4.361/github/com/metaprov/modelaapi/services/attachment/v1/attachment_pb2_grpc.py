# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from github.com.metaprov.modelaapi.services.attachment.v1 import attachment_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2


class AttachmentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListAttachments = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService/ListAttachments',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.ListAttachmentsRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.ListAttachmentsResponse.FromString,
                )
        self.CreateAttachment = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService/CreateAttachment',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.CreateAttachmentRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.CreateAttachmentResponse.FromString,
                )
        self.GetAttachment = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService/GetAttachment',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.GetAttachmentRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.GetAttachmentResponse.FromString,
                )
        self.UpdateAttachment = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService/UpdateAttachment',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.UpdateAttachmentRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.UpdateAttachmentResponse.FromString,
                )
        self.DeleteAttachment = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService/DeleteAttachment',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.DeleteAttachmentRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.DeleteAttachmentResponse.FromString,
                )


class AttachmentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListAttachments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAttachment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttachment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAttachment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAttachment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AttachmentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListAttachments': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAttachments,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.ListAttachmentsRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.ListAttachmentsResponse.SerializeToString,
            ),
            'CreateAttachment': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAttachment,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.CreateAttachmentRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.CreateAttachmentResponse.SerializeToString,
            ),
            'GetAttachment': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttachment,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.GetAttachmentRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.GetAttachmentResponse.SerializeToString,
            ),
            'UpdateAttachment': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAttachment,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.UpdateAttachmentRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.UpdateAttachmentResponse.SerializeToString,
            ),
            'DeleteAttachment': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteAttachment,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.DeleteAttachmentRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.DeleteAttachmentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AttachmentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListAttachments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService/ListAttachments',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.ListAttachmentsRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.ListAttachmentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateAttachment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService/CreateAttachment',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.CreateAttachmentRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.CreateAttachmentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttachment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService/GetAttachment',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.GetAttachmentRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.GetAttachmentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAttachment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService/UpdateAttachment',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.UpdateAttachmentRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.UpdateAttachmentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteAttachment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.attachment.v1.AttachmentService/DeleteAttachment',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.DeleteAttachmentRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_attachment_dot_v1_dot_attachment__pb2.DeleteAttachmentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
