import streamlit as st


class LogoutComponent:
    def render(self) -> bool:
        with st.sidebar:
            return st.button("Logout", type="primary", width="stretch")
