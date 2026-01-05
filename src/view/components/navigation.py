import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from typing import NamedTuple


class NavigationTabs(NamedTuple):
    home: DeltaGenerator
    insert: DeltaGenerator
    view: DeltaGenerator
    manage: DeltaGenerator


class NavigationComponent:
    def render(self) -> NavigationTabs:
        home, insert, view, manage = st.tabs(["Home", "Insert", "View", "Manage"])
        return NavigationTabs(home, insert, view, manage)
