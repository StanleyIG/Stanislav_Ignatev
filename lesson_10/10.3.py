class Cell:
    def __init__(self, cell):
        self.cell = cell


    def __add__(self, other):
        self.sum_cell = self.cell + other.cell
        return self.sum_cell


    def __sub__(self, other):
        self.sub_cell = self.cell - other.cell
        if self.sub_cell <= 0:
            return f'результат {self.sub_cell}, должно быть выше "0"'
        else:
            return f'результат вычитания {self.sub_cell}'



    def __mul__(self, other):
        self.mul_cell = self.cell * other.cell
        return self.mul_cell

    def __floordiv__(self, other):
        self.floordiv_cell = self.cell // other.cell
        return self.floordiv_cell

    def __truediv__(self, other):
        self.truediv_cell = self.cell / other.cell
        return self.truediv_cell

    def make_order(self, row):
        #return '\n'.join([row * '*' for i in range(round(self.cell / row))]) + "\n" + self.cell % row * '*'
        return ''.join([row * '*' + '|' for i in range(round(self.cell / row))]) + self.cell % row * '*'



add = Cell(20)
add_2 = Cell(15)
print(add + add_2)
sub = Cell(25)
sub_2 = Cell(26)
print(add - add_2)
print(sub - sub_2)

mul = Cell(9)
mul_2 = Cell(10)
print(mul * mul_2)
floordiv = Cell(36)
floordiv_2 = Cell(10)
print(floordiv // floordiv_2)
truediv = Cell(18)
truediv_2 = Cell(10)
print(truediv / truediv_2)
print(add.make_order(8))
print(add.make_order(5))
print(sub.make_order(5))

