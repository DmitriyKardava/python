my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for item in my_list:
    print(f"Привет, {item[item.rfind(' ')+1:len(item)].capitalize()}")
