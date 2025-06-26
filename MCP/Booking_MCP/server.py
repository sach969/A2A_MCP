from fastmcp import FastMCP
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Booking_MCP.mcp_tools.booking_tool import book_railway
from Booking_MCP.mcp_tools.booking_tool import book_hotel
from Booking_MCP.mcp_tools.booking_tool import book_cab

# Initialize the MCP server
mcp = FastMCP("Booking APP")

# Register tools
mcp.tool(description="""this tool will book railway ticket.""")(book_railway)

mcp.tool(description="""this tool will book hotel ticket.""")(book_hotel)

mcp.tool(description="""this tool will book a cab.""")(book_cab)


if __name__ == "__main__":
    mcp.run(transport="streamable-http",port=8001)