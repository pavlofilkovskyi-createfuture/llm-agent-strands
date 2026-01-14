# GitHubMCPClient is a wrapper for Starnds MCPClient to work with GitHub MCP Remote Server

usage: 
```python

import os
from wrapper import GitHubMCPClient

GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN")
github_mcp_client = GitHubMCPClient(access_token=GITHUB_ACCESS_TOKEN)

# call a single mcp tool manually
with github_mcp_client:
    result = github_mcp_client.call_tool_sync(tool_use_id="1", name="get_me", arguments={})
    print(result)

# but we normally want to use it a dependency for AWS Strands Agent:
from strands import Agent

with github_mcp_client:
    agent = Agent(
        tools=github_mcp_client.list_tools_sync(),
    )
    
    prompt = """
    list me titles of first 10 open issues in github repo: https://github.com/github/github-mcp-server
    """
    
    agent(prompt)
```