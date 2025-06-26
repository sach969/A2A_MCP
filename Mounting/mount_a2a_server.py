import sys
import os
import logging
from fastapi import FastAPI
from starlette.applications import Starlette

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from research_agent import server as research_server
from ticket_agent import ticket_server
from weather_agent import weather_Server 

research_app: Starlette = research_server.server.build(
    rpc_url="/a2a/request",
    agent_card_url="/.well-known/agent.json"
)
ticket_app: Starlette = ticket_server.server.build(
    rpc_url="/a2a/request",
    agent_card_url="/.well-known/agent.json"
)
weather_app: Starlette = weather_Server.server.build(
    rpc_url="/a2a/request",
    agent_card_url="/.well-known/agent.json"
)

# Create main FastAPI app
app = FastAPI(
    title="Combined A2A Server",
    description="All agents served from one FastAPI app",
    version="1.0",
)

# Mount the agent apps
app.mount("/research", research_app)
app.mount("/ticket", ticket_app)
app.mount("/weather", weather_app)


@app.get("/")
async def root():
    return {
        "status": "running",
        "a2a_routes": {
            "research": "/research/.well-known/agent.json",
            "ticket": "/ticket/.well-known/agent.json",
            "weather": "/weather/.well-known/agent.json"
        }
    }


if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Combined A2A Server on http://localhost:9999")
    uvicorn.run(app, host="0.0.0.0", port=9999)



