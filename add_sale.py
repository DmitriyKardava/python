from sys import argv
if len(argv) != 2:
    print("Укажите сумму")
    quit()
if not argv[1].replace('.', '', 1).isdigit():
    print("Неверная сумма")
    quit()
_str = f"{round(float(argv[1]), 2):>8.2f}\n"
if len(_str) > 9:
    print('Слишком большая сумма')
    quit()
print(f"'{_str}'")
with open('bakery.csv', 'a', encoding='utf-8') as sales:
    sales.write(_str)
