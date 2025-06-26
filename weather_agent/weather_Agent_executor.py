# research_agent/weather_agent_executor.py
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
from google import genai
import os

class WeatherAgentExecutor(AgentExecutor):
    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        user_input = context.get_user_input() or "What's the weather in Mohali?"

        gemini_client = genai.Client( api_key =os.getenv("GOOGLE_API_KEY"))
        transport = StreamableHttpTransport(url="http://localhost:8000/weather/mcp")
        mcp_client = Client(transport)

        async with mcp_client:
            prompt = f"""
            Your job is to choose and call the appropriate tool from the tools provided below to fulfill the user's request.
            Respond ONLY by calling the tool, DO NOT answer directly.Call Only One tool based on user query. Do not chain or repeat tool calls.

            User Input: {user_input}
            """
            try:
                response = await gemini_client.aio.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=prompt,
                    config=genai.types.GenerateContentConfig(
                        temperature=0.2,
                        tools=[mcp_client.session],
                    )
                )
                reply = str(response.candidates[0].content.parts[0].text)
            except Exception as e:
                reply = f"Error processing request via MCP: {e}"

        await event_queue.enqueue_event(new_agent_text_message(reply))

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        raise Exception("Cancel not supported")
