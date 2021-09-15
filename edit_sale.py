from sys import argv
if len(argv) != 3:
    print("edit_sale.py 'номер записи' сумма")
    quit()
if not argv[1].isdigit():
    print('Неверный номер записи')
    quit()
if not argv[2].replace('.', '', 1).isdigit():
    print("Неверная сумма")
    quit()
_str = f"{round(float(argv[2]), 2):>8.2f}\n"
if len(_str) > 9:
    print('Слишком большая сумма')
    quit()
_rec = int(argv[1])
_rec = _rec - 1 if _rec > 0 else 0
with open('bakery.csv', 'r+', encoding='utf-8') as sales:
    sales.seek(_rec * 10)
    if sales.readline().strip():
        sales.seek(sales.tell() - 10)
        sales.writelines(_str)
    else:
        print(f"Записи {_rec + 1} не существует")
