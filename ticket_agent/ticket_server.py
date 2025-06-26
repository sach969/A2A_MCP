import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCard, AgentCapabilities, AgentSkill
from ticket_agent.Ticket_agent_executor import TicketAgentExecutor

skill = AgentSkill(
    id="ticket_booking",
    name="Ticket Booking",
    description="Book tickets",
    tags=["ticket", "booking"],
)

agent_card = AgentCard(
    name="Ticket Agent",
    description="Books tickets for travel/events",
    url="http://localhost:9999/ticket",
    version="1.0.0",
    defaultInputModes=["text"],
    defaultOutputModes=["text"],
    capabilities=AgentCapabilities(streaming=True),
    skills=[skill],
)

request_handler = DefaultRequestHandler(
    agent_executor=TicketAgentExecutor(),
    task_store=InMemoryTaskStore(),
)

server = A2AStarletteApplication(
    agent_card=agent_card,
    http_handler=request_handler
)

# if __name__ == "__main__":
#     uvicorn.run(server.build(), host="0.0.0.0", port=9998)
