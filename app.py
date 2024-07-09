import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from tools import tools
from utils import process_tool_calls


load_dotenv()
st.title("💬 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "how may i help you"}
    ]
    st.session_state["all_messages"] = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    client = OpenAI()
    user_mesg = {"role": "user", "content": prompt}
    if len(st.session_state.all_messages) > 8:
        st.session_state.all_messages.pop(0)
        st.session_state.all_messages.pop(0)
    st.session_state.messages.append(user_mesg)
    st.session_state.all_messages.append(user_mesg)
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=st.session_state.all_messages, tools=tools
    )
    tool_calls = response.choices[0].message.tool_calls
    if tool_calls:
        messages = []
        messages.append(user_mesg)
        messages.append(response.choices[0].message)
        response = process_tool_calls(messages, tool_calls)
    if response:
        if type(response) == str:
            msg = json.loads(response)
        else:
            msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.session_state.all_messages.append({"role": "assistant", "content": str(msg)})
        st.chat_message("assistant").write(msg)
