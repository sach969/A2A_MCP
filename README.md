# A2A Research Chatbot

This is a simple A2A (Agent-to-Agent) powered chatbot that uses Google's **Gemini** language model to answer research questions. It features:

- A backend Research Agent using A2A protocol
- A frontend chatbot built in Streamlit
- Asynchronous communication using `httpx`
- Clean and minimal architecture for learning and prototyping

## Requirements

- OpenAI-compatible key for Gemini (via `langchain-google-genai`)

## Setup

1. Clone the repo and set up a virtual environment:
   ```bash
   git clone <your-repo-url># A2A Multi-Agent Chatbot

This project is a multi-agent chatbot system using the **A2A (Agent-to-Agent)** protocol, integrated with **MCP (Model Context Protocol)**. It supports multiple independent AI agents for different tasks, all mounted under a unified server.

---

## Project Overview

- **A2A Protocol**: Enables communication between agents using JSON-RPC.
- **MCP Integration**: Allows external tools and agents to interact with this system using a standardized protocol.
- **Agents Included**:
  - **Weather Agent** – provides current weather info
  - **Ticket Agent** – handles tickets
  - **Research Agent** – fetches summarized info

Each agent is built using `A2AStarletteApplication` and mounted inside a single FastAPI app.

---

## How to Run

### 1. Install dependencies

pip install -r requirements.txt

   cd a2a_chatbot
   python -m venv .venv
   source .venv/bin/activate 
   pip install -r requirements.txt

    Create a .env file in the root directory and add your Gemini API key:

    GOOGLE_API_KEY=your_google_genai_key_here

2. Run all agents from one server 

python Mounting/mount_combined_a2a_server.py

    Weather Agent: http://localhost:9999/weather

    Ticket Agent: http://localhost:9999/ticket

    Research Agent: http://localhost:9999/research

3. Run agents on separate ports

python Mounting/mount_multi_uvicorn.py

    Weather Agent: http://localhost:9997

    Ticket Agent: http://localhost:9998

    Research Agent: http://localhost:9999

4. Run the chatbot UI

streamlit run chatbot_ui/streamlit_ui.py


