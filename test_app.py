import streamlit as st

st.title("Hello Streamlit!")
st.write("This works without extra dependencies.")

name = st.text_input("Your name:")
if name:
    st.success(f"Hello {name}!")
