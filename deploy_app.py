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

# React to user input
if prompt := st.chat_input("What is up?"):
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

    # Add assistant response to display history
    st.session_state.display_messages.append({"role": "assistant", "content": response_message})

# Display chat messages from display history
for message in st.session_state.display_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
