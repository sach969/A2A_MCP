import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from MCP.weather_MCP import server as weather_server
from MCP.Booking_MCP import server as booking_server

from fastapi import FastAPI
from contextlib import AsyncExitStack, asynccontextmanager

# Instantiate individual FastAPI apps
weather_app = weather_server.mcp.http_app()
booking_app = booking_server.mcp.http_app()

@asynccontextmanager
async def lifespan(app):
    async with AsyncExitStack() as stack:
        await stack.enter_async_context(weather_app.lifespan(app))
        await stack.enter_async_context(booking_app.lifespan(app))
        yield

# Create the main combined app
app = FastAPI(
    title="Combined MCP Server",
    description="Running multiple MCP tool servers together",
    version="1.0",
    lifespan=lifespan,
)

# Mount individual apps
app.mount("/weather", weather_app)
app.mount("/booking", booking_app)

@app.get("/")
async def index():
    return {"status": "running", "routes": ["/weather", "/booking"]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
