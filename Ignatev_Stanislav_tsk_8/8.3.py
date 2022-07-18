from functools import wraps

def type_logger(func):
    @wraps(func)
    def wraper(*args):
        for i in args:
            b = f'{func.__name__}({i}: {type(i)}), value:{func(i),type(func(i))}'
            print(b)
    return wraper

@type_logger
def calc_cube(x):
    return x ** 3
a = calc_cube(5,6.5)
print(calc_cube)






