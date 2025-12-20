import streamlit as st
from typing import Any


class UploadFileComponent:
    def render(self, type: str) -> Any:
        if type == "Excel":
            return st.file_uploader(
                "File Uploader", type="xlsx", label_visibility="hidden"
            )
        elif type == "CSV":
            return st.file_uploader(
                "File Uploader", type="csv", label_visibility="hidden"
            )
