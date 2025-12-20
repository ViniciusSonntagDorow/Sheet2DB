import streamlit as st


class HeaderComponent:
    def render(self) -> None:
        st.header("💵 Spendly", anchor=False)
