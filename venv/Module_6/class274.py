from datetime import datetime

data_str2 = '25/09/2024'
data_fmt = '%d/%m/%Y'

# date = datetime(2024, 9, 25, 10, 29)
data = datetime.strptime(data_str2, data_fmt)
data_format = data.strftime(data_fmt)

print(data_format)
