from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, V, H):
        self.V = V
        self.H = H

    @abstractmethod
    def __str__(self):
        pass

    @property
    def general_calculation(self):
        return f'Общий подсчёт расхода ткани: {round(self.V / 6.5 + 0.5) + (2 * self.H + 0.3)}'

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
        self.calculation_coat = round(self.V / 6.5 + 0.5)

    def __str__(self):
        return f'Пальто: {self.calculation_coat}'


class Suit(Clothes):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.calculation_suit = round(2 * self.H + 0.3)

    def __str__(self):
        return f'Костюм: {self.calculation_suit}'


c = Coat(55, 175)
S = Suit(175, 55)
print(c)
print(S)
print(c.general_calculation)