from model.readers import CSVReader, ExcelReader
from model.validators import PanderaValidator
from model.loaders import PostgresLoader

csvreader = CSVReader()
excelreader = ExcelReader()
validator = PanderaValidator()
loader = PostgresLoader()

df = excelreader.read_data("./data/dados_corretos.xlsx")

validated_df = validator.validate_data(df)

print(loader)
