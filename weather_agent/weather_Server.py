import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCard, AgentCapabilities, AgentSkill
from weather_agent.weather_Agent_executor import WeatherAgentExecutor

skill = AgentSkill(
    id="Weather",
    name="Current_Weather",
    description="Give current weather",
    tags=["Weather","Temperature"],
)

agent_card = AgentCard(
    name="Weather Agent",
    description="Provide Current Weather",
    url="http://localhost:9999/weather",
    version="1.0.0",
    defaultInputModes=["text"],
    defaultOutputModes=["text"],
    capabilities=AgentCapabilities(streaming=True),
    skills=[skill],
)

request_handler = DefaultRequestHandler(
    agent_executor=WeatherAgentExecutor(),
    task_store=InMemoryTaskStore(),
)

server = A2AStarletteApplication(
    agent_card=agent_card,
    http_handler=request_handler
)

# if __name__ == "__main__":
#     uvicorn.run(server.build(), host="0.0.0.0", port=9997)
