import time

class TrafficLight:

    def __init__(self, color_1,color_2, color_3):
        self.color_1 = f'\033[31m{color_1}'
        self.color_2 = f'\033[33m{color_2}'
        self.color_3 = f'\033[32m{color_3}'


    def runing(self):
        print(self.color_1)
        time.sleep(7)
        print(self.color_2)
        time.sleep(2)
        print(self.color_3)
        time.sleep(10)

tfl = TrafficLight('red', 'yelow', 'green')
while True:
    tfl.runing()
