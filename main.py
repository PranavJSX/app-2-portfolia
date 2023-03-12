
import streamlit as st
import pandas

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

content2 = "Below you can fund some of the apps I have built in Python . Fell free to contact me."
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
# print(df)
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])