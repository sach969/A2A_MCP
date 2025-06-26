import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", 
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

async def route_to_agent(user_query: str) -> str:
    prompt = (
        "You are an intelligent router. Based on the user's query, decide which agent to route it to.\n"
        "Available agents: research, ticket, weather.\n"
        f"User Query: {user_query}\n"
        "Only respond with one word: research, ticket, or weather."
    )
    response = llm.invoke(prompt)
    return response.content.strip().lower()
