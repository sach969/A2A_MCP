import uvicorn

from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCard, AgentCapabilities, AgentSkill

from research_agent.agent_executer import ResearchAgentExecutor 

# 1. Define the skill
skill = AgentSkill(
    id="research_summary",
    name="Research Summarizer",
    description="Answers questions using Gemini",
    tags=["research", "llm", "gemini"],
    examples=["What is LangGraph?", "Explain Quantum Computing"],
)

# 2. Define the agent card
agent_card = AgentCard(
    name="Research Agent",
    description="Answers questions using LLM (Gemini)",
    url="http://localhost:9999/research",
    version="1.0.0",
    defaultInputModes=["text"],
    defaultOutputModes=["text"],
    capabilities=AgentCapabilities(streaming=True),
    skills=[skill],
)

# 3. Create the request handler and task store
request_handler = DefaultRequestHandler(
    agent_executor=ResearchAgentExecutor(),
    task_store=InMemoryTaskStore(),
)

# 4. Create the A2A application
server = A2AStarletteApplication(
    agent_card=agent_card,
    http_handler=request_handler
)

# # 5. Run the server
# if __name__ == "__main__":
#     uvicorn.run(server.build(), host="0.0.0.0", port=9999)
