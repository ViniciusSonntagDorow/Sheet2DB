import streamlit as st


class UploadOptionsComponent:
    def render(self):
        return st.selectbox(
            "Choose a file Type:",
            ("Excel", "CSV"),
        )
