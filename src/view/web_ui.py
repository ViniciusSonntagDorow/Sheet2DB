import streamlit as st

from view.components.header import HeaderComponent
from view.components.uploader import UploaderComponent
from view.components.navigator import NavigatorComponent


class WebUI:
    def __init__(self):
        self._set_page_config()
        self.header = HeaderComponent()
        self.uploader = UploaderComponent()
        self.navigator = NavigatorComponent()

    def _set_page_config(self):
        st.set_page_config(
            page_title="Sheet2DB",
            page_icon=":floppy_disk:",
            layout="centered",
            initial_sidebar_state="collapsed",
            menu_items={
                "About": "https://www.linkedin.com/in/viniciussonntagdorow/",
            },
        )

    def show_header(self):
        self.header.render()

    def show_navigation(self):
        return self.navigator.render()

    def get_uploaded_file(self):
        return self.uploader.render()
