import os
from dotenv import load_dotenv

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv() 

class ResearchAgentExecutor(AgentExecutor):
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        # Safe access to user input
        user_message = context.get_user_input() or "No input provided"

        # Gemini LLM call
        result = self.llm.invoke(user_message)

        # Send response back
        await event_queue.enqueue_event(
            new_agent_text_message(result.content)
        )

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        raise Exception("Cancel not supported")
