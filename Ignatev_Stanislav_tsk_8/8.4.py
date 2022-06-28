from functools import wraps


def type_logger(a=lambda x: x > 0):
    def _type_logger(func):
        @wraps(func)
        def wraper(x):
            try:
                if a(x):
                    b = f'{func.__name__}({x}: {type(x)}), value:{func(x), type(func(x))}'
                    return b
                else:
                    raise ValueError
            except ValueError:
                return f'ValueError: wrong email: {x}'
        return wraper

    return _type_logger


@type_logger(lambda x: x > 0)
def calc_cube(x):
    return x ** 3
print(calc_cube(5))
print(calc_cube(-5))
print(calc_cube)
