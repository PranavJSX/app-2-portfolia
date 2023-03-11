
import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=350)

with col2:
    st.title("Pranav Ojha")
    content = "Hi I am Pranav Ojha , I am a passionate learner who likes to learn and stay updated as much as I can " \
              ",I ger over excited when anything new is there to understand and work upon" \
              "Currently I am working for an insurance client in my current company and looking " \
              "to expand my skills for not just my proffesional growth but also my personal growth as well"
    st.write(content)