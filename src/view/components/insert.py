import streamlit as st
import datetime
from typing import Dict, Any

from utils.config import config


class InsertComponent:
    """Component for manual expense insertion form"""

    def render(self) -> Dict[str, Any]:
        """
        Render insert form and return data as dictionary.
        View's job: Display form and capture input.
        """
        st.subheader("Insert New Expense")

        with st.form("insert_expense_form"):
            date_input = st.date_input(
                "Date",
                value=datetime.datetime.today().date(),
                help="Select the expense date",
            )
            description_input = st.text_input(
                "Description",
                placeholder="e.g., Grocery shopping",
                help="Brief description of the expense",
            )
            category_input = st.selectbox(
                "Category", config.VALID_CATEGORIES, help="Select expense category"
            )
            amount_input = st.number_input(
                "Amount",
                min_value=0.0,
                step=0.01,
                format="%.2f",
                help="Enter the amount spent",
            )
            submit_button = st.form_submit_button("💾 Save Expense")

        # Return data as structured dictionary
        return {
            "date": date_input,
            "description": description_input,
            "category": category_input,
            "amount": amount_input,
            "submitted": submit_button,
        }
