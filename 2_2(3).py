my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(my_list))
for _i in range(len(my_list)):
    _sign = ''
    # пустая строка
    if my_list[_i]:
        # забыли кавычки
        my_list[_i] = str(my_list[_i])
        if my_list[_i][0] == '+' or my_list[_i][0] == '-':
            _sign = my_list[_i][0]
            my_list[_i] = my_list[_i][1:]
        if my_list[_i].isdigit():
            while len(my_list[_i]) < 2:
                my_list[_i] = '0' + my_list[_i]
        my_list[_i] = '"' + _sign + my_list[_i] + '"'
print(' '.join(my_list))
print(id(my_list))
