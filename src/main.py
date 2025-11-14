from model.readers import CSVReader, ExcelReader
from model.validators import PanderaValidator

csvreader = CSVReader()
excelreader = ExcelReader()

validator = PanderaValidator()

df = excelreader.read_data("./data/dados_corretos.xlsx")

validate = validator.validate_data(df)

print(validate)
