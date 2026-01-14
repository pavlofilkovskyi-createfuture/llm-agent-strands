import os
import sys
from strands.tools.mcp import MCPClient, MCPTransport
from mcp.client.stdio import stdio_client
from mcp import StdioServerParameters
from typing import Callable, cast

class GitMCPClient(MCPClient):

    def __init__(self):
        git_server_params = StdioServerParameters(
            command=sys.executable,
            args = ["-m", "mcp_server_git"],    # MCP Server
            env=os.environ.copy()               # Optional environment variables
        )

        cb = cast(Callable[[], MCPTransport], lambda: stdio_client(git_server_params))
        super().__init__(transport_callable=cb)