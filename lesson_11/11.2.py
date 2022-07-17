class ZeroDivisionError(Exception):
    def __init__(self, y):
        self.y = y

    def __str__(self):
        return f"ошибка ввода делителя, введите выше {self.y}"


class Division:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if self.y == 0:
            raise ZeroDivisionError(self.y)

    def division(self):
        def __init__(self, x, y):
            super().__init__(x, y)

        return self.x // self.y



try:
    div = Division(10, 0)
    print(div.division())
except ZeroDivisionError:
    print(f'введите делитель выше "0"')

