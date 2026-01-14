import os
from strands.tools.mcp import MCPClient, MCPTransport
from mcp.client.stdio import stdio_client
from mcp import StdioServerParameters
from typing import Callable, cast

class FilesystemMCPClient(MCPClient):

    def __init__(self):
        filesystem_server_params = StdioServerParameters(
            command = "npx",
            args = ["-y", "@modelcontextprotocol/server-filesystem", "/Users/pfilkovskyi/Projects"],
            env=os.environ.copy()
        )

        cb = cast(Callable[[], MCPTransport], lambda: stdio_client(filesystem_server_params))
        super().__init__(transport_callable=cb)