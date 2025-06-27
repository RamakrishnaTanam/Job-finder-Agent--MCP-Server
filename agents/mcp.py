# agents/mcp.py
class MCPServerStdio:
    async def __aenter__(self):
        print("Mock MCP Server started")
        return self
    async def __aexit__(self, exc_type, exc, tb):
        print("Mock MCP Server stopped")