import streamlit as st
import pandas as pd
from typing import Any, Dict, Optional


class DeleteFormComponent:
    def render(self, df: Optional[pd.DataFrame] = None) -> Dict[str, Any]:
        with st.form("delete_expenses_form"):
            st.subheader("Delete Expenses", anchor=False)

            selected_ids = st.multiselect(
                "Select Expenses to Delete",
                options=df["id"].tolist(),
                format_func=lambda x: f"""
                    {df[df["id"] == x]["id"].values[0]}, 
                    {df[df["id"] == x]["description"].values[0]}, 
                    {df[df["id"] == x]["category"].values[0]}, 
                    {df[df["id"] == x]["amount"].values[0]}, 
                    {df[df["id"] == x]["expense_date"].values[0]}
                """,
            )
            submit_button = st.form_submit_button(
                "Delete", width="stretch", type="primary"
            )
            return {
                "selected_ids": selected_ids,
                "submitted": submit_button,
            }
