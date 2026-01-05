import streamlit as st
import pandas as pd
from typing import Optional
import plotly.express as px


class DataViewComponent:
    def render(self, df: Optional[pd.DataFrame] = None) -> None:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                label="Total Expenses", value=f"€{df['amount'].sum():,.2f}", border=True
            )
        with col2:
            st.metric(label="Total Records", value=len(df), border=True)
        with col3:
            st.metric(
                label="Avg Amount", value=f"€{df['amount'].mean():,.2f}", border=True
            )

        category_data = (
            df.groupby(["category"])["amount"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

        date_data = (
            df.assign(expense_date=pd.to_datetime(df["expense_date"]).dt.normalize())
            .groupby(["expense_date"])["amount"]
            .sum()
            .reset_index()
            .sort_values("expense_date", ascending=True)
        )

        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.plotly_chart(
                    px.bar(
                        category_data,
                        x="category",
                        y="amount",
                        text="amount",
                    )
                    .update_traces(
                        textposition="outside",
                        texttemplate="€%{text:,.1f}",
                        textfont=dict(size=14),
                    )
                    .update_layout(
                        margin=dict(t=50, b=0, l=0, r=30),
                        yaxis=dict(title="", showgrid=False, showticklabels=False),
                        xaxis=dict(title="", tickfont=dict(size=14)),
                        title=dict(
                            text="Expenses by Category",
                            x=0,
                            xanchor="left",
                            font=dict(size=24),
                        ),
                    ),
                    config={"staticPlot": True},
                )
        with col2:
            with st.container(border=True):
                st.plotly_chart(
                    px.line(
                        date_data,
                        x="expense_date",
                        y="amount",
                    ).update_layout(
                        margin=dict(t=50, b=0, l=0, r=30),
                        yaxis=dict(title="", showgrid=False, showticklabels=False),
                        xaxis=dict(
                            title="",
                            tickfont=dict(size=14),
                            tickformat="%d %b",
                            dtick="D1",
                        ),
                        title=dict(
                            text="Expenses Over Time",
                            x=0,
                            xanchor="left",
                            font=dict(size=24),
                        ),
                    ),
                    # config={"staticPlot": True},
                )

        with st.container(border=True):
            st.subheader("Recent Expenses", anchor=False)
            st.dataframe(
                date_data.sort_values("expense_date", ascending=False).head(20),
            )
            print(date_data.head(20))
            print(date_data.info())
