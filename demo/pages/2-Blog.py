import streamlit as st
import time
import numpy as np
import os

st.set_page_config(page_title="", page_icon="🌍")

st.sidebar.header("[Blog Post](top)")

BLOG_FILE_PATH = os.path.join(os.path.dirname(__file__),"2-blog.md")
with open(BLOG_FILE_PATH,"r") as _f:
    content = _f.read()
st.markdown(content)
