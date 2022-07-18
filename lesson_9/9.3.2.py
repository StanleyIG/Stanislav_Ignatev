class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage,
                       "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_fullname(self):
        print(f'{self.name} {self.surname}: {self.position}')

    def get_total_income(self):
        if isinstance (self._income["wage"], int or float) and (self._income["bonus"], int or float):
            for i,v in self._income.items():
                print(i,v)

t = Position('Иван', 'Иванов', 'сантехник', 10000, 90000)
t.get_fullname()
t.get_total_income()

t_2 = Position('John', 'Smith', 'кузнец', 10000, 100000)
t_2.get_fullname()
t_2.get_total_income()