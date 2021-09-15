from sys import argv

if not argv[1].isdigit() or int(argv[1]) <= 0:
    quit()
_str_num = 0
with open('bakery_v2.csv', 'r+', encoding='utf-8') as sales, \
        open('_tail.tmp', 'w', encoding='utf-8') as _tmp:
    for sale in sales:
        _str_num += 1
        if _str_num > int(argv[1]):
            _tmp.write(sale)
    if _str_num < int(argv[1]):
        print(f"Строка {argv[1]} не найдена")
        quit()
_str_num = 0
with open('bakery_v2.csv', 'r', encoding='utf-8') as sales:
    while _str_num < int(argv[1]) - 1:
        sales.readline()
        _str_num += 1
    _seek_point = sales.tell()

with open('bakery_v2.csv', 'ab') as sales:
    sales.seek(_seek_point)
    sales.truncate()

with open('bakery_v2.csv', 'a', encoding='utf-8') as sales, \
        open('_tail.tmp', 'r', encoding='utf-8') as _tmp:
    sales.write(f"{argv[2].strip()}\n")
    for _line in _tmp:
        sales.write(_line)
