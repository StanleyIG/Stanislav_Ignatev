import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = ['на право', 'на лево', 'прямо', 'в магазин']

    def go(self):
        print(f'автомобиль "{self.color} {self.name}" поехал')

    def stop(self):
        print(f'автомобиль "{self.color} {self.name}" остановилcя')

    def turn(self):
        print(f'автомобиль "{self.color} {self.name}" поехал {random.choice(self.direction)}')

    def show_speed(self):
        print(f'скорость "{self.color} {self.name}" {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed >= 61:
            print(f'скорость "{self.color} {self.name}" {self.speed} км/ч - превышение скорости!')
        else:
            print(f'скорость "{self.color} {self.name}" {self.speed} км/ч')
    def police(self):
        if self.is_police:
                print('полицейская машина')
        else:
            print('гражданский автомобиль')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            print('полицейская машина')
        else:
            print('гражданский автомобиль')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed >= 41:
            print(f'скорость "{self.color} {self.name}" {self.speed} км/ч - превышение скорости!')
        else:
            print(f'скорость "{self.color} {self.name}" {self.speed} км/ч')
        def police(self):
            if self.is_police:
                print('полицейская машина')
            else:
                print('гражданский автомобиль')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            print('полицейская машина')
        else:
            print('гражданский автомобиль')

town = TownCar(60, 'чёрный', 'Toyota Camry', False)
town.go()
town.turn()
town.show_speed()
town.stop()
town.police()
print('==============================')
sport = SportCar(60, 'жёлтая', 'Ламба', False)
sport.go()
sport.turn()
sport.show_speed()
sport.stop()
sport.police()
print('==============================')
work = WorkCar(40, 'белый', 'Hyundai, такси', False)
work.go()
work.turn()
work.show_speed()
work.stop()
sport.police()
print('==============================')
policecar = PoliceCar(60, 'Полиция', 'Ford', True)
policecar.go()
policecar.turn()
policecar.show_speed()
policecar.stop()
policecar.police()

