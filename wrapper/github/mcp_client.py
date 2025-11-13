from strands.tools.mcp import MCPClient
from mcp.client.streamable_http import streamablehttp_client

class GitHubMCPClient(MCPClient):
    
    GITHUB_MCP_ENDPOINT = "https://api.githubcopilot.com/mcp"
    
    def __init__(self, access_token: str):
        if not access_token:
            raise ValueError("`access_token` must be provided")
        
        auth_headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json"
        }
        
        super().__init__(
            lambda: streamablehttp_client(
                url=self.GITHUB_MCP_ENDPOINT,
                headers=auth_headers
            )
        )