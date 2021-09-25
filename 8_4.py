from functools import wraps


def val_checker(l_func):

    def wrapper(func):

        @wraps(func)
        def _check(num):
            if l_func(num):
                return func(num)
            else:
                raise ValueError(f'Неверное значение {num}')
        return _check
    return wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x**3


try:
    print(calc_cube(7))
except(ValueError, TypeError) as err:
    print(err)
print(help(calc_cube))
