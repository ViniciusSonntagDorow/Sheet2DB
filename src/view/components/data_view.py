import streamlit as st
import pandas as pd
from typing import Optional


class DataViewComponent:
    def render(self, df: Optional[pd.DataFrame] = None) -> None:
        st.subheader("📊 Expense Analytics")

        if df is None or df.empty:
            st.info("No data available yet. Upload or insert expenses first.", icon="ℹ️")
            return

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Expenses", f"${df['amount'].sum():,.2f}")
        with col2:
            st.metric("Total Records", len(df))
        with col3:
            st.metric("Avg Amount", f"${df['amount'].mean():,.2f}")

        st.subheader("Expenses by Category")
        category_data = (
            df.groupby("category")["amount"].sum().sort_values(ascending=False)
        )
        st.bar_chart(category_data)

        st.subheader("Recent Expenses")
        st.dataframe(
            df.sort_values("date", ascending=False).head(20), use_container_width=True
        )
