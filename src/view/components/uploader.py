import streamlit as st


class UploaderComponent:
    def render(self):
        return st.file_uploader(
            "File Uploader", type=["xlsx", "csv"], label_visibility="hidden"
        )
