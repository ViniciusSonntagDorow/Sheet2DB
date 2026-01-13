import streamlit as st


class LoginComponent:
    def render(self) -> bool:
        with st.sidebar:
            return st.button("Login", type="primary", width="stretch")
