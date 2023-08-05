# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from github.com.metaprov.modelaapi.services.reciperun.v1 import reciperun_pb2 as github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2


class RecipeRunServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListRecipeRuns = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService/ListRecipeRuns',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.ListRecipeRunsRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.ListRecipeRunsResponse.FromString,
                )
        self.CreateRecipeRun = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService/CreateRecipeRun',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.CreateRecipeRunRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.CreateRecipeRunResponse.FromString,
                )
        self.GetRecipeRun = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService/GetRecipeRun',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.GetRecipeRunRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.GetRecipeRunResponse.FromString,
                )
        self.UpdateRecipeRun = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService/UpdateRecipeRun',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.UpdateRecipeRunRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.UpdateRecipeRunResponse.FromString,
                )
        self.DeleteRecipeRun = channel.unary_unary(
                '/github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService/DeleteRecipeRun',
                request_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.DeleteRecipeRunRequest.SerializeToString,
                response_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.DeleteRecipeRunResponse.FromString,
                )


class RecipeRunServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListRecipeRuns(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRecipeRun(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRecipeRun(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRecipeRun(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRecipeRun(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecipeRunServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListRecipeRuns': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRecipeRuns,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.ListRecipeRunsRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.ListRecipeRunsResponse.SerializeToString,
            ),
            'CreateRecipeRun': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRecipeRun,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.CreateRecipeRunRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.CreateRecipeRunResponse.SerializeToString,
            ),
            'GetRecipeRun': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRecipeRun,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.GetRecipeRunRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.GetRecipeRunResponse.SerializeToString,
            ),
            'UpdateRecipeRun': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRecipeRun,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.UpdateRecipeRunRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.UpdateRecipeRunResponse.SerializeToString,
            ),
            'DeleteRecipeRun': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRecipeRun,
                    request_deserializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.DeleteRecipeRunRequest.FromString,
                    response_serializer=github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.DeleteRecipeRunResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RecipeRunService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListRecipeRuns(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService/ListRecipeRuns',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.ListRecipeRunsRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.ListRecipeRunsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateRecipeRun(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService/CreateRecipeRun',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.CreateRecipeRunRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.CreateRecipeRunResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRecipeRun(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService/GetRecipeRun',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.GetRecipeRunRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.GetRecipeRunResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRecipeRun(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService/UpdateRecipeRun',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.UpdateRecipeRunRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.UpdateRecipeRunResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRecipeRun(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.metaprov.modelaapi.services.reciperun.v1.RecipeRunService/DeleteRecipeRun',
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.DeleteRecipeRunRequest.SerializeToString,
            github_dot_com_dot_metaprov_dot_modelaapi_dot_services_dot_reciperun_dot_v1_dot_reciperun__pb2.DeleteRecipeRunResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
