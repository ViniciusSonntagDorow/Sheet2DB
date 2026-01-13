import streamlit as st

if not st.user.is_logged_in:
    st.button("Log in with Google", on_click=st.login, args=["google"])
else:
    st.button("Log out", on_click=st.logout)
    st.write(f"Hello, {st.user.name}!")
