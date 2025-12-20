import streamlit as st
from typing import Any


class UploadOptionsComponent:
    def render(self) -> Any:
        return st.selectbox("Choose a file Type:", ("Excel", "CSV"), index=None)
