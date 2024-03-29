# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from userwatch import userwatch_historian_pb2 as userwatch_dot_userwatch__historian__pb2


class HistorianStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReportLogEntry = channel.unary_unary(
                '/uwGrpc.Historian/ReportLogEntry',
                request_serializer=userwatch_dot_userwatch__historian__pb2.LogEntry.SerializeToString,
                response_deserializer=userwatch_dot_userwatch__historian__pb2.LogEntryResponse.FromString,
                )


class HistorianServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReportLogEntry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HistorianServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReportLogEntry': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportLogEntry,
                    request_deserializer=userwatch_dot_userwatch__historian__pb2.LogEntry.FromString,
                    response_serializer=userwatch_dot_userwatch__historian__pb2.LogEntryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'uwGrpc.Historian', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Historian(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReportLogEntry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uwGrpc.Historian/ReportLogEntry',
            userwatch_dot_userwatch__historian__pb2.LogEntry.SerializeToString,
            userwatch_dot_userwatch__historian__pb2.LogEntryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
