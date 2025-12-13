import streamlit as st


class NavigateComponent:
    def render(self):
        home, insert, upload, view, manage = st.tabs(
            ["Home", "Insert", "Upload", "View", "Manage"]
        )
        return home, insert, upload, view, manage
