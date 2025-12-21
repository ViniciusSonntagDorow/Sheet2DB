import streamlit as st


class HomeComponent:
    def render(self) -> None:
        st.subheader("Welcome to Spendly!", anchor=False)
        st.markdown(
            """
            This application helps you track your expenses.
            """
        )
        st.subheader("Features:", anchor=False)
        st.markdown(
            """
            - Insert individual expense records manually.
            - Upload bulk expense data via CSV or Excel files.
            - View and analyze your expense data with interactive charts and tables.
            - Manage categories and settings to customize your experience.
            """
        )
