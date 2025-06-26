import httpx
from uuid import uuid4
from a2a.client import A2AClient, A2ACardResolver
from a2a.types import MessageSendParams, SendMessageRequest
from client.router import route_to_agent

AGENT_URLS = {
    "research": "http://localhost:9999/research",
    "ticket": "http://localhost:9999/ticket",
    "weather": "http://localhost:9999/weather",
}

async def query_dynamic_agent(user_query: str) -> str:
    agent_key = await route_to_agent(user_query)
    base_url = AGENT_URLS.get(agent_key)

    if not base_url:
        return f"No agent found for: {agent_key}"

    async with httpx.AsyncClient(timeout=30.0) as httpx_client:
        resolver = A2ACardResolver(httpx_client=httpx_client, base_url=base_url)
        card = await resolver.get_agent_card() 
        agent_name = card.name 

        client = A2AClient(httpx_client=httpx_client, agent_card=card)

        payload = {
            "message": {
                "role": "user",
                "parts": [{"kind": "text", "text": user_query}],
                "messageId": uuid4().hex,
            }
        }

        request = SendMessageRequest(id=str(uuid4()), params=MessageSendParams(**payload))
        response = await client.send_message(request)

        message = response.root.result.parts
        text_parts = [part.root.text for part in message if part.root.kind == "text"]
        response_text = "\n".join(text_parts) if text_parts else "Agent replied, but no text found."

        return f"{agent_name}\n\n{response_text}"


