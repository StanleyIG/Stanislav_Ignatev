class Worker:
    def __init__(self):
        self.name = ['Пётр', 'Иван']
        self.surname = ['Васильев', 'Иванов']
        self.position = ['сантехник', 'строитель']
        self.income = {"wage": (1000, 2000),
                  "bonus": (5000, 3000)}


class Position(Worker):

    def get_fullname(self):
        self.list_fullname = []
        fullname = (f'{a} {b}: {c},' for a,b,c in zip(self.name, self.surname, self.position))
        for i in fullname:
            self.list_fullname.append(i)

    def get_total_income(self):
        self.list_income = []
        for i in range(len(self.income.values())):
            wage = self.income['wage'][i]
            bonus = self.income['bonus'][i]
            result = wage + bonus
            self.list_income.append(result)
        over = [f'{i} сумарный доход(оклад + бонусы) {v} рублей' for i,v in zip(self.list_fullname,self.list_income)]
        for i in over:
            print(i)


t = Position()
t.get_fullname()
t.get_total_income()



