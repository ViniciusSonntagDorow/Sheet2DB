import streamlit as st


class NavigatorComponent:
    def render(self):
        col1, col2 = st.columns([1, 1])
        with col1:
            btn_insert = st.button(
                "Insert Data", width="stretch", icon=":material/upload:"
            )
        with col2:
            btn_view = st.button(
                "View Data", width="stretch", icon=":material/bar_chart:"
            )

        if btn_insert:
            return "INSERT"
        if btn_view:
            return "VIEW"
        return None
