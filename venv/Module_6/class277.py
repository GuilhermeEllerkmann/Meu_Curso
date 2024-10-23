from datetime import datetime

fmt = '%d/%m/%Y'
fmt2 = '%d/%m/%Y %H:%M'
fmt3 = '%d/%m/%Y %H:%M:%S'
fmt4 = '%Y'
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime(fmt))
print(data.strftime(fmt2))
print(data.strftime(fmt3))
print(data.strftime(fmt4))
print(data.year)
