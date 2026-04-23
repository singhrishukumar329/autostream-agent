import streamlit as st
from agent import run_agent

st.title("AutoStream AI Agent")

user_input = st.text_input("Enter your query:")

if user_input:
    response = run_agent(user_input)
    st.write(response)