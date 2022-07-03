class Road:
    def __init__(self):
        self._length = 5000
        self._width = 20
        self.m = 25


    def calc_asphalt(self,t):
        self.t = t
        print(round(self._width * self._length * self.m * t / 1000), 'т')

a = Road()
a.calc_asphalt(5)
