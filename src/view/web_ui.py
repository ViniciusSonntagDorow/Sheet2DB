import streamlit as st

from view.components.header import HeaderComponent
from view.components.upload_file import UploadFileComponent
from view.components.upload_options import UploadOptionsComponent
from view.components.navigate import NavigateComponent
from view.components.view import ViewComponent
from view.components.home import HomeComponent
from view.components.insert import InsertComponent
from view.components.manage import ManageComponent


class WebUI:
    def __init__(self):
        self._set_page_config()
        self.header = HeaderComponent()
        self.upload = UploadFileComponent()
        self.upload_options = UploadOptionsComponent()
        self.navigator = NavigateComponent()
        self.view = ViewComponent()
        self.home = HomeComponent()
        self.insert = InsertComponent()
        self.manage = ManageComponent()

    def _set_page_config(self):
        st.set_page_config(
            page_title="Spendly",
            page_icon="💵",
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

    def show_home(self):
        return self.home.render()

    def show_insert(self):
        return self.insert.render()

    def get_uploaded_file(self, type: str):
        return self.upload.render(type)

    def get_uploaded_option(self):
        return self.upload_options.render()

    def show_view(self):
        return self.view.render()

    def show_manage(self):
        return self.manage.render()
