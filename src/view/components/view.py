import streamlit as st
import pandas as pd
from typing import Optional


class ViewComponent:
    """Component for displaying and analyzing expense data"""

    def render(self, df: Optional[pd.DataFrame] = None):
        """
        Display data view with charts and tables.
        View's job: Just display the data provided by controller.
        """
        st.subheader("📊 Expense Analytics")

        if df is None or df.empty:
            st.info("No data available yet. Upload or insert expenses first.", icon="ℹ️")
            return

        # Display metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Expenses", f"${df['amount'].sum():,.2f}")
        with col2:
            st.metric("Total Records", len(df))
        with col3:
            st.metric("Avg Amount", f"${df['amount'].mean():,.2f}")

        # Display charts
        st.subheader("Expenses by Category")
        category_data = (
            df.groupby("category")["amount"].sum().sort_values(ascending=False)
        )
        st.bar_chart(category_data)

        # Display table
        st.subheader("Recent Expenses")
        st.dataframe(
            df.sort_values("date", ascending=False).head(20), use_container_width=True
        )
