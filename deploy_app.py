import streamlit as st
import configparser
import tiktoken
import openai

# OpenAI APIの初期化
openai.api_key = st.secrets.OpenAI.API_KEY

st.title("Echo Bot - 家庭教師")

# Initialize chat history and tokens history
if "display_messages" not in st.session_state:
    st.session_state.display_messages = []
if "query_history" not in st.session_state:
    st.session_state.query_history = []
if "total_tokens" not in st.session_state:
    st.session_state.total_tokens = 0

# Display chat messages from display history
for message in st.session_state.display_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container immediately
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to display history
    st.session_state.display_messages.append({"role": "user", "content": prompt})

    # OpenAI APIによる応答の取得
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "user", "content": prompt}
        ]
    )
    response_message = response.choices[0].message['content'].strip()

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response_message)
    # Add assistant response to display history
    st.session_state.display_messages.append({"role": "assistant", "content": response_message})

    # Add to query history
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    tokens = len(encoding.encode(prompt))
    st.session_state.query_history.append({"role": "user", "content": prompt, "tokens": tokens})
    st.session_state.total_tokens += tokens

    tokens = len(encoding.encode(response_message))
    st.session_state.query_history.append({"role": "assistant", "content": response_message, "tokens": tokens})
    st.session_state.total_tokens += tokens

    # Ensure total tokens in query history is under 1000
    while st.session_state.total_tokens > 1000:
        removed_item = st.session_state.query_history.pop(0)  # Remove oldest entry
        st.session_state.total_tokens -= removed_item["tokens"]

    # Print query history and tokens for debug purposes
    for item in st.session_state.query_history:
        print(f"Role: {item['role']}, Content: {item['content']}, Tokens: {item['tokens']}")
