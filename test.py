import streamlit as st
st.title("My first stream lit app")
name=st.text_input("Enter your name")
if st.button("Submit"):
  st.write(f"Hello, {name}")
age=st.text_input("Enter your age")
if age>=18:
  st.write("You are eligible to vote")
  
