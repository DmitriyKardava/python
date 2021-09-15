from sys import argv
_start_rec = 1
_end_rec = 1

if len(argv) == 2 and argv[1].isdigit():
    _start_rec = int(argv[1])
elif len(argv) == 3 and argv[1].isdigit() and argv[2].isdigit():
    _start_rec = int(argv[1])
    _end_rec = int(argv[2])
else:
    print("show_sales.py начальная запись (конечная запись)")
    quit()

_start_rec = _start_rec - 1 if _start_rec > 0 else 0
_end_rec = _end_rec - 1 if _end_rec > 0 else 0

with open('bakery.csv', 'r', encoding='utf-8') as sales:
    sales.seek(_start_rec * 10)
    for _rec in sales:
        _start_rec += 1
        print(f"{(_rec.strip())}")
        if _end_rec and _start_rec > _end_rec:
            break
