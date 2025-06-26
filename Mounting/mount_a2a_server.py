import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from research_agent import server as research_server
from ticket_agent import ticket_server
from weather_agent import weather_Server

from fastapi import FastAPI

research_app = research_server.server
ticket_app = ticket_server.server
a2a_weather_app = weather_Server.server

# Create the main FastAPI app
app = FastAPI(
    title="Combined A2A Agent Server",
    description="Unified deployment of multiple A2A agents",
    version="1.0",
)

# Mount A2A agents at unique prefixes
app.mount("/research", research_app)
app.mount("/ticket", ticket_app)
app.mount("/weather", a2a_weather_app)

# Health check
@app.get("/")
async def root():
    return {
        "status": "running",
        "a2a_routes": {
            "research_agent": "/research",
            "ticket_agent": "/ticket",
            "weather_agent": "/weather"
        }
    }

# Run with: python mount_a2a_agents.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9999)

