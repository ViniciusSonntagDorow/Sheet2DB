from model.csv_reader import CSVReader
from model.excel_reader import ExcelReader
from model.pandera_validator import PanderaValidator
from model.postgres_loader import PostgresLoader

csvreader = CSVReader()
excelreader = ExcelReader()
validator = PanderaValidator()
loader = PostgresLoader()

df = excelreader.read_data("../data/dados_corretos.xlsx")

validated_df = validator.validate_data(df)

print(loader)
