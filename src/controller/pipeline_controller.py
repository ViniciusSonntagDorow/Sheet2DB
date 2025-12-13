from model.csv_reader import CSVReader
from model.excel_reader import ExcelReader
from model.pandera_validator import PanderaValidator
from model.postgres_loader import PostgresLoader

from view.web_ui import WebUI


class PipelineController:
    def __init__(self, view: WebUI):
        self.view = view

        self.csv_reader = CSVReader()
        self.excel_reader = ExcelReader()
        self.validator = PanderaValidator()
        self.loader = PostgresLoader()

    def run(self):
        self.view.show_header()

        home, insert, upload, view, manage = self.view.show_navigation()

        with home:
            self._home_flow()

        with insert:
            self._insert_flow()

        with upload:
            self._upload_flow()

        with view:
            self._view_flow()

        with manage:
            self._manage_flow()

    def _home_flow(self):
        self.view.show_home()

    def _insert_flow(self):
        date_imput, description_input, category_input, amount_input, submit_button = self.view.show_insert()

    def _upload_flow(self):
        uploaded_option = self.view.get_uploaded_option()
        uploaded_file = self.view.get_uploaded_file(uploaded_option)

    def _view_flow(self):
        self.view.show_view()

    def _manage_flow(self):
        self.view.show_manage()
