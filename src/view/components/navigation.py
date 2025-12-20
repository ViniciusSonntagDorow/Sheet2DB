import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from typing import NamedTuple


class NavigationTabs(NamedTuple):
    home: DeltaGenerator
    insert: DeltaGenerator
    upload: DeltaGenerator
    view: DeltaGenerator
    manage: DeltaGenerator


class NavigationComponent:
    def render(self) -> NavigationTabs:
        home, insert, upload, view, manage = st.tabs(
            ["Home", "Insert", "Upload", "View", "Manage"]
        )
        return NavigationTabs(home, insert, upload, view, manage)
