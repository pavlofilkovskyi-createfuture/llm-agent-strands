# Test communication with the GitHub Remote MCP Server
See documentation here first: https://github.com/github/github-mcp-server

1. send handshake:
    - end-point: https://api.githubcopilot.com/mcp
    - headers:
        - Content-Type: application/json
    - body:
        ```json
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2025-06-18",
                "capabilities": { },
                "clientInfo": {
                    "name": "pavlofilkovskyi-createfuture",
                    "version": "0.1.0"
                }
            }
        }
        ```
2. list tools:
    - end-point: https://api.githubcopilot.com/mcp
    - headers: 
        - Content-Type: application/json
        - mcp-session-id: `<get this header from the response to the Initialization request above>`
    - body:
        ```json
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list",
            "params": { }
        }
        ```

3. call tool (for instance: `get_me`):
    - end-point: https://api.githubcopilot.com/mcp
    - headers: 
        - Content-Type: application/json
        - mcp-session-id: `<get this header from the response to the Initialization request above>`
    - body:
        ```json
        {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "get_me",
                "arguments": { }
            }
        }
        ```

for more options see [github-mcp-server/.../\_\_toolsnaps\_\_](https://github.com/github/github-mcp-server/tree/main/pkg/github/__toolsnaps__)