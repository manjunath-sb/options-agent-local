from mcp.client.streamable_http import streamable_http_client
from strands.tools.mcp.mcp_client import MCPClient


def create_mcp_client():
    def create_transport():
        return streamable_http_client("http://localhost:8000/mcp/")

    return MCPClient(create_transport)
