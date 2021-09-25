from functools import wraps


def type_logger(func):
    @wraps(func)
    def type_wrapper(*args, **kwargs):
        print(f'{func.__name__}(', end='')
        args_list = [i for i in (*args, *kwargs.values())]
        n = (f"{el}: {type(el)}" for el in args_list)
        print(*n, sep=', ', end='')
        print(')')
        return func(*args, **kwargs)
    return type_wrapper


@type_logger
def calc_cube(*x, **y):
    params = [i for i in (*x, *y.values()) if isinstance(i, int) or isinstance(i, float)]
    return [i ** 3 for i in params]


print(*calc_cube(1, 2, 3, 4, 5, {1, 2}, [0, 3], 'sdf'))
help(calc_cube)
