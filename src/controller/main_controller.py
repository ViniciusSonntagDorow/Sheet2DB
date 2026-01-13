import streamlit as st
from view.streamlit_view import StreamlitView
from controller.home_controller import HomeController
from controller.insert_controller import InsertController
from controller.dashboard_controller import DashboardController
from controller.delete_controller import DeleteController


class MainController:
    def __init__(
        self,
        view: StreamlitView,
        home_controller: HomeController,
        insert_controller: InsertController,
        dashboard_controller: DashboardController,
        delete_controller: DeleteController,
    ):
        self._view = view
        self._home_controller = home_controller
        self._insert_controller = insert_controller
        self._dashboard_controller = dashboard_controller
        self._delete_controller = delete_controller

    def execute(self) -> None:
        if not self._view.is_logged_in():
            if self._view.show_login():
                st.login("google")
            return

        else:
            if self._view.show_logout():
                st.logout()

        self._view.show_header()

        tabs = self._view.show_navigation()

        with tabs.home:
            self._home_controller.execute()

        with tabs.insert:
            self._insert_controller.execute()

        with tabs.dashboard:
            self._dashboard_controller.execute()

        with tabs.delete:
            self._delete_controller.execute()
