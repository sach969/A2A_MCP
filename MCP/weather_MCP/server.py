from fastmcp import FastMCP
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from MCP.weather_MCP.mcp_tools.weather_tool import weather


# Initialize the MCP server
mcp = FastMCP("Registration APP")

# Register tools
mcp.tool(description="""this tool will give the weather update.""")(weather)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")