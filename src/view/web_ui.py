import streamlit as st
import pandas as pd
from typing import Optional, Dict, Any

from view.components.header import HeaderComponent
from view.components.upload_file import UploadFileComponent
from view.components.upload_options import UploadOptionsComponent
from view.components.navigation import NavigationComponent
from view.components.data_view import DataViewComponent
from view.components.home import HomeComponent
from view.components.insert_form import InsertFormComponent
from view.components.manage import ManageComponent


class WebUI:
    def __init__(self):
        self._set_page_config()
        self.header = HeaderComponent()
        self.upload = UploadFileComponent()
        self.upload_options = UploadOptionsComponent()
        self.navigation = NavigationComponent()
        self.data_view = DataViewComponent()
        self.home = HomeComponent()
        self.insert_form = InsertFormComponent()
        self.manage = ManageComponent()

    def _set_page_config(self) -> None:
        st.set_page_config(
            page_title="Spendly",
            page_icon="💵",
            layout="wide",
            initial_sidebar_state="auto",
            menu_items={
                "About": "https://www.linkedin.com/in/viniciussonntagdorow/",
            },
        )

    def show_header(self) -> None:
        self.header.render()

    def show_navigation(self) -> Any:
        return self.navigation.render()

    def show_home(self) -> Any:
        return self.home.render()

    def get_insert_form(self) -> Optional[Dict[str, Any]]:
        return self.insert_form.render()

    def get_upload_option(self) -> Optional[str]:
        return self.upload_options.render()

    def get_uploaded_file(self, file_type: str) -> Any:
        return self.upload.render(file_type)

    def show_data_view(self, df: pd.DataFrame) -> None:
        self.data_view.render(df)

    def show_manage(self) -> Any:
        return self.manage.render()

    def show_dataframe_preview(self, df: pd.DataFrame) -> None:
        st.subheader("Data Preview", anchor=False)
        st.dataframe(df.head(5))

    def show_success(self, message: str) -> None:
        st.balloons()
        st.toast(message, icon="✅", duration="short")

    def show_error(self, message: str) -> None:
        st.error(message, icon="🚨")

    def show_warning(self, message: str) -> None:
        st.warning(message, icon="⚠️")

    def show_info(self, message: str) -> None:
        st.info(message, icon="ℹ️")

    def ask_confirmation(self, question: str) -> bool:
        return st.button(question, width="stretch", type="primary")
