import streamlit as st
import pandas as pd
from dataclasses import dataclass
import plotly.express as px


@dataclass
class DashboardData:
    """Data transfer object with pre-calculated dashboard data."""

    total_expenses: float
    total_records: int
    avg_amount: float
    max_amount: float
    category_data: pd.DataFrame
    date_data: pd.DataFrame
    recent_expenses: pd.DataFrame


class DashboardComponent:
    def render(self, data: DashboardData) -> None:
        """Renders dashboard - View only displays, no calculations."""
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                label="Total Expenses",
                value=f"€{data.total_expenses:,.2f}",
                border=True,
            )
        with col2:
            st.metric(label="Total Records", value=data.total_records, border=True)
        with col3:
            st.metric(label="Avg Amount", value=f"€{data.avg_amount:,.2f}", border=True)

        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.subheader("Expenses by Category", anchor=False)
                st.plotly_chart(
                    px.bar(
                        data.category_data,
                        x="category",
                        y="amount",
                        text="amount",
                    )
                    .update_traces(
                        textposition="auto",
                        texttemplate="€%{text:,.2f}",
                        textfont=dict(size=14),
                    )
                    .update_layout(
                        margin=dict(t=0, b=0, l=0, r=30),
                        yaxis=dict(title="", showgrid=False, showticklabels=False),
                        xaxis=dict(title="", tickfont=dict(size=14)),
                    ),
                    config={"staticPlot": True},
                )
        with col2:
            with st.container(border=True):
                st.subheader("Expenses Over Time", anchor=False)
                st.plotly_chart(
                    px.line(
                        data.date_data,
                        x="expense_date",
                        y="amount",
                    ).update_layout(
                        margin=dict(t=0, b=0, l=0, r=30),
                        yaxis=dict(
                            title="",
                            showgrid=False,
                            showticklabels=True,
                        ),
                        xaxis=dict(
                            title="",
                            tickfont=dict(size=14),
                            tickformat="%d %b",
                            dtick="D1",
                        ),
                    ),
                    config={"staticPlot": True},
                )

        with st.container(border=True):
            st.subheader("Recent Expenses", anchor=False)
            st.dataframe(
                data.recent_expenses,
                hide_index=True,
                column_config={
                    "expense_date": st.column_config.DateColumn(
                        "Date",
                        format="DD/MM/YYYY",
                    ),
                    "description": "Description",
                    "category": "Category",
                    "amount": st.column_config.ProgressColumn(
                        "Amount (€)",
                        format="€%.2f",
                        min_value=0,
                        max_value=data.max_amount,
                    ),
                },
            )
