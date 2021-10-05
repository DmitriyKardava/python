class MyZeroDivisionError(Exception):
    msg = "Деление на ноль запрещено"

    def __str__(self):
        return self.msg


class MyFloat(float):

    def __truediv__(self, other):
        if other is not None and other == 0:
            raise MyZeroDivisionError
        return MyFloat(float(self) / float(other))


while True:
    try:
        user_input = []
        while len(user_input) != 2:
            user_input = input("Введите делимое и делитель через пробел или stop: ")
            if user_input:
                if user_input.lower() == 'stop':
                    raise SystemExit
                else:
                    user_input = user_input.split()
        dividend, divider = map(MyFloat, user_input)
        print(dividend / divider)
    except MyZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)
        # break
