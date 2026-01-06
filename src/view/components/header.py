import streamlit as st


class HeaderComponent:
    def render(self) -> None:
        with st.sidebar:
            st.title("💵 Spendly", anchor=False)
