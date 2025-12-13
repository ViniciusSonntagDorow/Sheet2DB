import streamlit as st
import datetime


class InsertComponent:
    def render(self):
        with st.form("form"):
            date_imput = st.date_input("Date", value=datetime.datetime.today().date())
            description_input = st.text_input("Description")
            category_input = st.selectbox(
                "Category", [
                    "Supermarket",
                    "Transport",
                    "Entertainment",
                    "Shopping",
                    "Bills",
                    "Health",
                    "Education",
                    "Other",
                    ]
            )
            amount_input = st.number_input("Amount", min_value=0.0)
            submit_button = st.form_submit_button("Submit")
        return date_imput, description_input, category_input, amount_input, submit_button
