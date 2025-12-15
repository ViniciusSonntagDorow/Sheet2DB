import streamlit as st
import pandas as pd
from typing import Optional, Dict, Any

from view.components.header import HeaderComponent
from view.components.upload_file import UploadFileComponent
from view.components.upload_options import UploadOptionsComponent
from view.components.navigate import NavigateComponent
from view.components.view import ViewComponent
from view.components.home import HomeComponent
from view.components.insert import InsertComponent
from view.components.manage import ManageComponent


class WebUI:
    """
    View layer - responsible ONLY for displaying data and capturing user input.
    No business logic should be here.
    """

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
            initial_sidebar_state="expanded",
            menu_items={
                "About": "https://www.linkedin.com/in/viniciussonntagdorow/",
            },
        )

    # ===== Display Methods =====

    def show_header(self):
        """Display application header"""
        self.header.render()

    def show_navigation(self):
        """Display navigation tabs"""
        return self.navigator.render()

    def show_home(self):
        """Display home page"""
        return self.home.render()

    def show_manage(self):
        """Display manage page"""
        return self.manage.render()

    # ===== User Input Methods =====

    def get_insert_form_data(self) -> Optional[Dict[str, Any]]:
        """
        Get form data from insert component.
        Returns dict with form fields and submitted status.
        """
        return self.insert.render()

    def get_upload_option(self) -> Optional[str]:
        """Get selected file upload type (CSV/Excel)"""
        return self.upload_options.render()

    def get_uploaded_file(self, file_type: str):
        """Get uploaded file from user"""
        return self.upload.render(file_type)

    # ===== Data Display Methods =====

    def show_data_view(self, df: pd.DataFrame):
        """Display data visualization with dataframe"""
        self.view.render(df)

    def show_dataframe_preview(self, df: pd.DataFrame):
        """Show preview of dataframe before processing"""
        st.subheader("Data Preview")
        st.dataframe(df.head(10))
        st.info(f"Total records: {len(df)}")

    # ===== Feedback Methods =====

    def show_success(self, message: str):
        """Display success message"""
        st.success(message, icon="✅")

    def show_error(self, message: str):
        """Display error message"""
        st.error(message, icon="🚨")

    def show_warning(self, message: str):
        """Display warning message"""
        st.warning(message, icon="⚠️")

    def show_info(self, message: str):
        """Display info message"""
        st.info(message, icon="ℹ️")

    # ===== Interaction Methods =====

    def ask_confirmation(self, question: str) -> bool:
        """Ask user for confirmation"""
        return st.button(question)
