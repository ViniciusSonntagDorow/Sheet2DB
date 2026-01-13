import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from typing import NamedTuple


class NavigationTabs(NamedTuple):
    home: DeltaGenerator
    insert: DeltaGenerator
    dashboard: DeltaGenerator
    delete: DeltaGenerator


class NavigationComponent:
    def render(self) -> NavigationTabs:
        home, insert, delete, dashboard = st.tabs(
            ["Overview", "Insert Expense", "Delete Expense", "Dashboard"]
        )
        return NavigationTabs(home, insert, dashboard, delete)
