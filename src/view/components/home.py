import streamlit as st


class HomeComponent:
    def render(self):
        # info = st.error("Under Development...", icon="🚨")
        text = st.markdown(
            """
            ### Welcome to Expense Tracker App!
            This application helps you track your expenses efficiently.

            ### Features:
            - Insert individual expense records manually.
            - Upload bulk expense data via CSV or Excel files.
            - View and analyze your expense data with interactive charts and tables.
            - Manage categories and settings to customize your experience.

            ### Developed by:
            - Vinicius Sonntag Dorow | [GitHub](https://github.com/ViniciusSonntagDorow) | [LinkedIn](https://www.linkedin.com/in/viniciussonntagdorow/)
            """
        )
        return text
