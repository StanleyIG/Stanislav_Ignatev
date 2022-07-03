import time

class TrafficLight:
    __color = ['\033[31m {}'.format(''), '\033[33m {}'.format(''), '\033[32m {}'.format('')]

    def runing(self, a, b, c):
        self.a = a
        for i in t.__color:
            if '\033[31m' in i:
                print(i, a)
                time.sleep(5)
        self.b = b
        for i in t.__color:
            if '\033[33m' in i:
                print(i, b)
                time.sleep(2)
        self.c = c
        for i in t.__color:
            if '\033[32m' in i:
                print(i, c)
                time.sleep(5)
t = TrafficLight()
while True:
    t.runing('стой', 'готовься', 'поехали')
