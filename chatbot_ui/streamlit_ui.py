import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import asyncio
from client.a2a_client import query_dynamic_agent

st.title("Multi-Agent Chatbot")

user_input = st.text_input("Ask your question:")

if user_input:
    with st.spinner("Thinking..."):
        response = asyncio.run(query_dynamic_agent(user_input))
    st.markdown(f"**Bot:** {response}")
