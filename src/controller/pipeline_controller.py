import os
import tempfile
from typing import Any

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

        action = self.view.show_navigation()

        if action == "INSERT":
            self._handle_insert_flow()
        elif action == "VIEW":
            self._handle_view_flow()

    def _handle_insert_flow(self):
        uploaded_file = self.view.get_uploaded_file()

        if uploaded_file:
            if self.view.is_process_button_clicked():
                self._run_etl_pipeline(uploaded_file)

    def _handle_view_flow(self):
        self.view.show_info("Funcionalidade de visualização em desenvolvimento.")

    def _run_etl_pipeline(self, uploaded_file: Any):
        temp_path = None

        try:
            with self.view.show_spinner("Iniciando processamento..."):
                temp_path = self._save_temp_file(uploaded_file)

                df = self._read_file_strategy(uploaded_file.name, temp_path)

                self.view.show_info("Validando dados...")
                df_validado = self.validator.validate_data(df)

                self.view.show_info("Carregando no banco de dados...")
                self.loader.load_data(df_validado, "tabela_vendas")

                self.view.show_success("Processo concluído com sucesso!")
                self.view.show_data(df_validado)

        except ValueError as e:
            self.view.show_error(f"Erro de Leitura: {e}")

        except Exception as e:
            self.view.show_error(f"Falha no Pipeline: {e}")

        finally:
            if temp_path and os.path.exists(temp_path):
                os.remove(temp_path)

    def _save_temp_file(self, uploaded_file) -> str:
        suffix = f".{uploaded_file.name.split('.')[-1]}"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.getbuffer())
            return tmp.name

    def _read_file_strategy(self, filename: str, filepath: str):
        if filename.endswith(".csv"):
            return self.csv_reader.read_data(filepath)
        elif filename.endswith(".xlsx"):
            return self.excel_reader.read_data(filepath)
        else:
            raise ValueError("Formato de arquivo não suportado.")
