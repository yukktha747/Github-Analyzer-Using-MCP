import asyncio
import streamlit as st

from agent import GitHubAgent


st.set_page_config(
    page_title="GitHub AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 GitHub AI Assistant")
st.markdown(
    "Analyze GitHub profiles using **MCP + OpenRouter + GitHub API**"
)

# Initialize agent
if "agent" not in st.session_state:
    st.session_state.agent = GitHubAgent()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input(
    "Ask about any GitHub profile..."
)

if prompt:

    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):

        with st.spinner("Analyzing GitHub profile..."):

            answer = asyncio.run(
                st.session_state.agent.ask(prompt)
            )

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )