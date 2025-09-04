import streamlit as st


class ExcelValidadorUI:
    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title="Excel schema validator",
            page_icon=":floppy_disk:",
            layout="centered",
            initial_sidebar_state="collapsed",
            menu_items={
                "About": "https://www.linkedin.com/in/viniciussonntagdorow/",
            },
        )

    def display_header(self):
        st.title("Insert your excel for validation")

    def upload_file(self):
        return st.file_uploader("Load your excel file here", type=["xlsx"])

    def display_results(self, result, error):
        if error:
            st.error(f"Validation error: {error}")
        else:
            st.success("The excel schema is correct!")

    def display_save_button(self):
        return st.button("Save to database")

    def display_wrong_message(self):
        return st.error("Need to correct the excel!")

    def display_success_message(self):
        return st.success("Data saved successfully to the database!")
