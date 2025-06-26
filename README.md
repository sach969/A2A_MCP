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
   git clone <your-repo-url>
   cd a2a_chatbot
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   pip install -r requirements.txt

    Create a .env file in the root directory and add your Gemini API key:

    GOOGLE_API_KEY=your_google_genai_key_here

Running the Project
Step 1: Start the Research Agent

python -m research_agent.server

This will start the A2A Agent on http://localhost:9999.

Step 2: Run the Streamlit Chat UI

In a new terminal, run:

streamlit run chatbot/streamlit.py

