from utils import currency_rates
from sys import argv
if len(argv) > 1 and currency_rates(argv[1]):
    _val, _date = currency_rates(argv[1])
    print(f"{_val}, {_date}")
else:
    print('Ошибка')
