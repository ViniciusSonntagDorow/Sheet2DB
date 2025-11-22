import streamlit as st

from components.header import HeaderComponent
from components.uploader import UploaderComponent


class WebUI:
    def __init__(self):
        self.set_page_config()
        HeaderComponent()
        UploaderComponent()

    def set_page_config(self):
        st.set_page_config(
            page_title="Sheet2DB",
            page_icon=":floppy_disk:",
            layout="centered",
            initial_sidebar_state="collapsed",
            menu_items={
                "About": "https://www.linkedin.com/in/viniciussonntagdorow/",
            },
        )


WebUI()
