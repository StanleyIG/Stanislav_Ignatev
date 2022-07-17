

class ComplexNumber:
    def __init__(self, number):
        self.number = number



    def __add__(self, other):
        self.res = self.number + other.number
        return self.res

    def __mul__(self, other):

        self.res2 = self.number * other.number
        return self.res2

    def __str__(self):
        return f'сложение {self.res} умножеие {self.res2}'




complexnumber = ComplexNumber(55)
complexnumber2 = ComplexNumber(77)
complexnumber + complexnumber2
complexnumber * complexnumber2
print(complexnumber)




