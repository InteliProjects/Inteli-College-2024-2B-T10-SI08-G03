import streamlit as st

class Header:
    def __init__(self, title):
        self.title = title

    def render(self):
        st.markdown(
            f"<h1 style='text-align: center; color: #4CAF50;'>{self.title}</h1>",
            unsafe_allow_html=True
        )
