import streamlit as st


st.write('Hello')

name = st.text_input("What's your name?")


st.title(name)