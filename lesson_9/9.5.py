class Stationery:
    def __init__(self,title):
        self. title = title

    def __draw(self):
        print('«Запуск отрисовки»')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}\nрисунок ручкой')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title}\nрисунок карандашём')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'{self.title}\nрисунок маркером')


pen = Pen('ручка')
pensil = Pencil('карандаш')
handle = Handle('Маркер')

pen._Stationery__draw()
pen.draw()
pensil._Stationery__draw()
pensil.draw()
handle._Stationery__draw()
handle.draw()


