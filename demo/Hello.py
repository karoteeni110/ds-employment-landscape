import streamlit as st

st.set_page_config(
    page_title="Hello!",
    page_icon="👋",
)

st.write("""# Welcome to Data Science Employment ~~Landscape~~ Snapshot!""")

st.sidebar.success("Select a demo above.")

with open("hello.md","r") as _f:
    content = _f.read()
st.markdown(content)