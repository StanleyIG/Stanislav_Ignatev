import re

class Data(object):

    def __init__(self, d=0, m=0, y=0):
        self.d = d
        self.m = m
        self.y = y


    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 1920 <= year <= 2022:
                    return f'{data}'
                else:
                    return f'Некоректный год {year}'
            else:
                return f'Число месяца {month} должно быть не более 12'
        else:
            return f'Число дня {day} должно быть не более 31 '



    @classmethod
    def convert_data(cls, data):
        day,month,year = map(int, re.findall('\d+', data))
        return cls.validation(day,month,year), f'Дата: {day}\nМесяц: {month}\nГод: {year}'



data = Data()
convert = Data.convert_data('31-12-2022')
print(convert)



