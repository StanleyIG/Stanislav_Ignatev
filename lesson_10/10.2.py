from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, V, H):
        self.V = V
        self.H = H

    @abstractmethod
    def calculation(self):
        pass


    @property
    def general_calculation(self):
        return f'Общая площадь ткани: {round(self.V / 6.5 + 0.5) + (2 * self.H + 0.3)}'

    @property
    def V(self):
        return self.__V

    @V.setter
    def V(self, V):
        if V > 65:
            self.__V = 65
        elif V < 45:
            self.__V = 45
        else:
            self.__V = V

    @property
    def H(self):
        return self.__H

    @H.setter
    def H(self, H):
        if H > 185:
            self.__H = 185
        elif H < 140:
            self.__H = 145
        else:
            self.__H = H




class Coat(Clothes):
    def __init__(self, V, H):
        super().__init__(V, H)

    def calculation(self):
        return f'пальто {round(self.V / 6.5 + 0.5)}'



class Suit(Clothes):
    def __init__(self, V, H):
        super().__init__(V, H)


    def calculation(self):
        return f'костюм {round(2*self.H + 0.3)}'





c = Coat(55,175)
s = Suit(175,55)
print(c.calculation())
print(s.calculation())
print(c.general_calculation)






