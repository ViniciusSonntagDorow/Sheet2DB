import streamlit as st


class HeaderComponent:
    def render(self) -> None:
        st.title("💵 Spendly", anchor=False)
