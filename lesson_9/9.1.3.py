import time
class TrafficLight:


    class TrafficLight:
        def __init__(self, color_1, color_2, color_3):
            self.__color = [[5,'\033[31m {}'.format(color_1)], [2,'\033[33m {}'.format(color_2)],
                            [7,'\033[32m {}'.format(color_3)], [2,'\033[33m {}'.format(color_2)]]

        def runing(self):
            for i in self.__color:
                print(f'\r{i[1]}', end="")
                time.sleep(i[0])

    t = TrafficLight('red', 'yelow', 'green')
    while True:
        t.runing()
