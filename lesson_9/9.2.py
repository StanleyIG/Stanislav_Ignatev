class Road:

    def __init__(self, length, width,t):
        _length = length
        _width = width
        self.m = 25
        self.t = t
        print(round(_width * _length * self.m * t / 1000), 'т')
r = Road(5000, 20, 5)





