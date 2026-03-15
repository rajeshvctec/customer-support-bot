import streamlit as st
from rag_chain import get_answer

st.set_page_config(
    page_title="Customer Support Bot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Customer Support Assistant")
st.caption("Ask me anything about our products and services.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and message.get("sources"):
            with st.expander("📄 Sources"):
                for src in message["sources"]:
                    st.write(f"• {src}")

if user_input := st.chat_input("Type your question here..."):

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Searching documents..."):
            response = get_answer(user_input)

        st.markdown(response["answer"])

        if response["sources"]:
            with st.expander("📄 Sources"):
                for src in response["sources"]:
                    st.write(f"• {src}")

    st.session_state.messages.append({
        "role": "assistant",
        "content": response["answer"],
        "sources": response["sources"]
    })
