import streamlit as st
import pandas as pd
from typing import Optional, Dict, Any

from view.components.header import HeaderComponent
from view.components.navigation import NavigationComponent, NavigationTabs
from view.components.dashboard import DashboardComponent, DashboardData
from view.components.home import HomeComponent
from view.components.insert_form import InsertFormComponent
from view.components.delete_form import DeleteFormComponent
from view.components.login import LoginComponent
from view.components.logout import LogoutComponent


class StreamlitView:
    def __init__(self):
        self._configure_page()
        self._header = HeaderComponent()
        self._navigation = NavigationComponent()
        self._dashboard = DashboardComponent()
        self._home = HomeComponent()
        self._insert_form = InsertFormComponent()
        self._delete_form = DeleteFormComponent()
        self._login = LoginComponent()
        self._logout = LogoutComponent()

    def _configure_page(self) -> None:
        st.set_page_config(
            page_title="Spendly",
            page_icon="💵",
            layout="wide",
            initial_sidebar_state="auto",
            menu_items={
                "About": "https://www.linkedin.com/in/viniciussonntagdorow/",
            },
        )
        st.markdown(
            """
            <style>
                .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                }
            </style>
        """,
            unsafe_allow_html=True,
        )

    # === Layout Methods ===

    def show_header(self) -> None:
        self._header.render()

    def show_navigation(self) -> NavigationTabs:
        return self._navigation.render()

    def show_home(self) -> None:
        self._home.render()

    def show_dashboard(self, data: DashboardData) -> None:
        self._dashboard.render(data)

    def show_login(self) -> bool:
        return self._login.render()

    def show_logout(self) -> bool:
        return self._logout.render()

    # === Form Methods ===

    def get_insert_form(self) -> Optional[Dict[str, Any]]:
        return self._insert_form.render()

    def get_delete_form(self, df: Optional[pd.DataFrame] = None) -> Dict[str, Any]:
        return self._delete_form.render(df)

    # === Feedback Methods ===

    def show_success(self, message: str) -> None:
        st.balloons()
        st.toast(message, icon="✅")

    def show_error(self, message: str) -> None:
        st.error(message, icon="🚨")

    def show_warning(self, message: str) -> None:
        st.warning(message, icon="⚠️")

    def show_info(self, message: str) -> None:
        st.info(message, icon="ℹ️")

    # === Utility Methods ===

    def show_dataframe_preview(self, df: pd.DataFrame) -> None:
        st.subheader("Data Preview", anchor=False)
        st.dataframe(df.head(5))

    def refresh(self) -> None:
        st.rerun()

    def is_logged_in(self) -> bool:
        return st.user.is_logged_in
