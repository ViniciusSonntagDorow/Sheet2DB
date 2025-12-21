import streamlit as st
import datetime
from typing import Optional, Dict, Any

from utils.config import config


class InsertFormComponent:
    def render(self) -> Optional[Dict[str, Any]]:
        with st.form("insert_expense_form"):
            st.subheader("Insert New Expense", anchor=False)
            col1, col2 = st.columns(2)
            with col1:
                date_input = st.date_input(
                    "Date",
                    value=datetime.datetime.today().date(),
                    help="Select the expense date",
                )
            with col2:
                description_input = st.text_input(
                    "Description",
                    placeholder="e.g., Grocery shopping",
                    help="Brief description of the expense",
                )
            with col2:
                category_input = st.selectbox(
                    "Category", config.VALID_CATEGORIES, help="Select expense category"
                )
            with col1:
                amount_input = st.number_input(
                    "Amount",
                    min_value=0.0,
                    step=0.01,
                    format="%.2f",
                    help="Enter the amount spent",
                )
            submit_button = st.form_submit_button(
                "Save Expense", width="stretch", type="primary"
            )

        return {
            "date": date_input,
            "description": description_input,
            "category": category_input,
            "amount": amount_input,
            "submitted": submit_button,
        }
