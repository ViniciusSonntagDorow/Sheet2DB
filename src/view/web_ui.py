import streamlit as st
import pandas as pd
from typing import Optional, Dict, Any

from view.components.header import HeaderComponent
from view.components.navigation import NavigationComponent, NavigationTabs
from view.components.dashboard import DashboardComponent
from view.components.home import HomeComponent
from view.components.insert_form import InsertFormComponent
from view.components.delete_form import DeleteFormComponent


class WebUI:
    def __init__(self):
        self._set_page_config()
        self.header = HeaderComponent()
        self.navigation = NavigationComponent()
        self.dashboard = DashboardComponent()
        self.home = HomeComponent()
        self.insert_form = InsertFormComponent()
        self.delete_form = DeleteFormComponent()

    def _set_page_config(self) -> None:
        st.set_page_config(
            page_title="Spendly",
            page_icon="💵",
            layout="wide",
            initial_sidebar_state="expanded",
            menu_items={
                "About": "https://www.linkedin.com/in/viniciussonntagdorow/",
            },
        )

    def show_header(self) -> None:
        self.header.render()

    def show_navigation(self) -> NavigationTabs:
        return self.navigation.render()

    def show_home(self) -> Any:
        return self.home.render()

    def get_insert_form(self) -> Optional[Dict[str, Any]]:
        return self.insert_form.render()

    def show_dashboard(self, df: pd.DataFrame) -> None:
        self.dashboard.render(df)

    def get_delete_form(self, df: Optional[pd.DataFrame] = None) -> Dict[str, Any]:
        return self.delete_form.render(df)

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
