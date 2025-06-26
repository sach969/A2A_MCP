from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
from google import genai

GEMINI_API_KEY = "AIzaSyDXi2ifbugToNiIqEkv4fRazUPVn_4Hnno"  
gemini_client = genai.Client(api_key=GEMINI_API_KEY)
transport = StreamableHttpTransport(url="http://localhost:8000/booking/mcp")
mcp_client = Client(transport)

class TicketAgentExecutor(AgentExecutor):
    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        user_input = context.get_user_input() or "Book a ticket for Sachin"

        async with mcp_client:
            prompt = f"""
            You are an intelligent booking assistant.

            Your job is to:
            Choose and call ONLY ONE tool from the available tools.

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
                print(response)

                tool_result = None
                text_result = None

                # Loop through parts
                parts = response.candidates[0].content.parts
                for part in parts:
                    if hasattr(part, "function_response") and part.function_response:
                        content_list = part.function_response.response.get("result", {}).get("content", [])
                        if content_list:
                            tool_result = content_list[0].text
                            break
                    elif hasattr(part, "text") and part.text:
                        text_result = part.text

                reply = tool_result or text_result or "No tool response or text returned."

            except Exception as e:
                reply = f"Error: {e}"

        await event_queue.enqueue_event(new_agent_text_message(reply))

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        raise Exception("Cancel not supported")
