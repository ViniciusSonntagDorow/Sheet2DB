import streamlit as st


class UploaderComponent:
    def __init__(self):
        self.upload_file()

    def upload_file(self):
        return st.file_uploader("", type=["xlsx", "csv"])
