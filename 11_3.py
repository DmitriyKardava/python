class NotNumber(ValueError):
    msg = 'Введите число'

    def __str__(self):
        return self.msg


my_list = []
while True:
    try:
        value = input('Добавьте число в список или stop:')
        if value == 'stop':
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as e:
        print(e)
print(my_list)
