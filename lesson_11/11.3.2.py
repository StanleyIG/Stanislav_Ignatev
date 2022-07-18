class ListError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'тип {self.data} явлется {type(self.data)} введите число'


class NewList:
    def __init__(self, data):
        self.data = data

while True:
    try:
        res = []
        while True:
            number = input()
            if number.isdigit():
                res.append(int(number))
            elif number == 'q':
                quit(res)
            elif number:
                raise ListError(number)
    except ListError:
        print('только целые числа')




