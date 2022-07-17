import json


class Officeequipment:
    def __init__(self, is_old, new, repair, type):  # состояние, тип оргтехники
        self.is_old = is_old
        self.new = new
        self.repair = repair
        self.type = type


class Printer(Officeequipment):
    def __init__(self, is_old, new, repair, type, name, count):
        super().__init__(is_old, new, repair, type)
        self.name = name
        self.count = count

    def description_printer(self):
        if self.is_old or self.new or self.repair:
            return f'принтер {self.name}, колличество {self.count}'


class Scanner(Officeequipment):
    def __init__(self, is_old, new, repair, type, name, count):  # название, габариты, состояние
        super().__init__(is_old, new, repair, type)
        self.name = name
        self.count = count

    def description_scanner(self):
        if self.is_old or self.new or self.repair:
            return f'сканер {self.name}, колличество {self.count}'


class Copier(Officeequipment):
    def __init__(self, is_old, new, repair, type, name, count):
        # состояние, тип, название, габариты, колличество
        super().__init__(is_old, new, repair, type)
        self.name = name
        self.count = count

    def description_copier(self):
        return f'{self.type}, брэнд: {self.name}, колличество {self.count}'


class SubErr(Exception):
    def __init__(self, data, data2):
        self.data = data
        self.data2 = data2

    def __str__(self):
        return f'запрашиваемое колличество {self.data}, на складе:{self.data2}'


class OfficeEquipmenWarehouse:
    FILENAME = 'OfficeEquipmenWarehouse.json'
    res = {'старая оргтехника': {},
           'новая оргтехника': {},
           'нужен ремонт': {}}

    while True:
        choose = input('добавить/списать(нажмите "q" чтобы выйти): ')
        if choose == 'добавить':
            choose2 = input('выбирите тип оргтехники(ксерокс, принтер, сканер): ')
            if choose2 == 'ксерокс':
                name_exm = '1'
                name_exm += name_exm
                state = input('является ли ксерокс старым(да/нет): ')
                if state == 'да':
                    state = True
                else:
                    state = False
                state2 = input('является ли ксерокс новым(да/нет): ')
                if state2 == 'да':
                    state2 = True
                else:
                    state2 = False
                state3 = input('требуется ремонт ?(да/нет): ')
                if state3 == 'да':
                    state3 = True
                else:
                    state3 = False
                cop = input('(ксерокс)введите тип: ')
                cop2 = input('(ксерокс)введите название: ')
                cop3 = input('(ксерокс)введите колличество ')
                name_exm = Copier(state, state2, state3, cop, cop2, int(cop3))
                if name_exm.is_old:
                    res['старая оргтехника'].setdefault(name_exm.name, []).append(name_exm.description_copier())
                    res['старая оргтехника'][name_exm.name].append(name_exm.count)
                    with open(FILENAME, 'r+', encoding='utf-8') as file:
                        try:
                            data = json.load(file)
                            data['старая оргтехника'][name_exm.name] = [name_exm.description_copier(), name_exm.count]
                            print(data)
                            with open(FILENAME, 'r+', encoding='utf-8') as file:
                                json.dump(data, file, ensure_ascii=False, indent=4)
                        except json.JSONDecodeError:
                            json.dump(res, file, ensure_ascii=False, indent=4)
                elif name_exm.new:
                    res['новая оргтехника'].setdefault(name_exm.name, []).append(name_exm.description_copier())
                    res['новая оргтехника'][name_exm.name].append(name_exm.count)
                    with open(FILENAME, 'r+', encoding='utf-8') as file2:
                        try:
                            data = json.load(file2)
                            data['новая оргтехника'][name_exm.name] = [name_exm.description_copier(), name_exm.count]
                            print(data)
                            with open(FILENAME, 'r+', encoding='utf-8') as file2:
                                json.dump(data, file2, ensure_ascii=False, indent=4)
                        except json.JSONDecodeError:
                            json.dump(res, file2, ensure_ascii=False, indent=4)
                elif name_exm.repair:
                    res['требуется ремонт'].setdefault(name_exm.name, []).append(name_exm.description_copier())
                    res['требуется ремонт'][name_exm.name].append(name_exm.count)
                    with open(FILENAME, 'r+', encoding='utf-8') as file3:
                        try:
                            data = json.load(file3)
                            data['требуется ремонт'][name_exm.name] = [name_exm.description_copier(), name_exm.count]
                            print(data)
                            with open(FILENAME, 'r+', encoding='utf-8') as file3:
                                json.dump(data, file3, ensure_ascii=False, indent=4)
                        except json.JSONDecodeError:
                            json.dump(res, file3, ensure_ascii=False, indent=4)

            elif choose2 == 'принтер':
                name_exm = '2'
                name_exm += name_exm
                state_printer = input('является ли принтер старым(да/нет): ')
                if state_printer == 'да':
                    state_printer = True
                else:
                    state_printer = False
                state_printer2 = input('является ли принтер новым(да/нет): ')
                if state_printer2 == 'да':
                    state_printer2 = True
                else:
                    state_printer2 = False
                state_printer3 = input('требуется ремонт ?(да/нет): ')
                if state_printer3 == 'да':
                    state_printer3 = True
                else:
                    state_printer3 = False
                pr = input('(принтер)введите тип: ')
                pr2 = input('(принтер)введите название: ')
                pr3 = input('(принтер)введите колличество ')
                name_exm = Printer(state_printer, state_printer2, state_printer3, pr, pr2, int(pr3))
                if name_exm.is_old:
                    res['старая оргтехника'].setdefault(name_exm.name, []).append(name_exm.description_printer())
                    res['старая оргтехника'][name_exm.name].append(name_exm.count)
                    with open(FILENAME, 'r+', encoding='utf-8') as file:
                        try:
                            data = json.load(file)
                            data['старая оргтехника'][name_exm.name] = [name_exm.description_printer(), name_exm.count]
                            print(data)
                            with open(FILENAME, 'r+', encoding='utf-8') as file:
                                json.dump(data, file, ensure_ascii=False, indent=4)
                        except json.JSONDecodeError:
                            json.dump(res, file, ensure_ascii=False, indent=4)
                elif name_exm.new:
                    res['новая оргтехника'].setdefault(name_exm.name, []).append(name_exm.description_printer())
                    res['новая оргтехника'][name_exm.name].append(name_exm.count)
                    with open(FILENAME, 'r+', encoding='utf-8') as file:
                        try:
                            data = json.load(file)
                            data['новая оргтехника'][name_exm.name] = [name_exm.description_printer(), name_exm.count]
                            print(data)
                            with open(FILENAME, 'r+', encoding='utf-8') as file:
                                json.dump(data, file, ensure_ascii=False, indent=4)
                        except json.JSONDecodeError:
                            json.dump(res, file, ensure_ascii=False, indent=4)

                elif name_exm.repair:
                    res['требуется ремонт'].setdefault(name_exm.name, []).append(name_exm.description_printer())
                    res['требуется ремонт'][name_exm.name].append(name_exm.count)
                    with open(FILENAME, 'r+', encoding='utf-8') as file:
                        try:
                            data = json.load(file)
                            data['требуется ремонт'][name_exm.name] = [name_exm.description_printer(), name_exm.count]
                            print(data)
                            with open(FILENAME, 'r+', encoding='utf-8') as file:
                                json.dump(data, file, ensure_ascii=False, indent=4)
                        except json.JSONDecodeError:
                            json.dump(res, file, ensure_ascii=False, indent=4)
            elif choose2 == 'сканер':
                name_exm = '3'
                name_exm += name_exm
                state_scanner = input('является ли принтер старым(да/нет): ')
                if state_scanner == 'да':
                    state_scanner = True
                else:
                    state_scanner = False
                state_scanner2 = input('является ли принтер новым(да/нет): ')
                if state_scanner2 == 'да':
                    state_scanner2 = True
                else:
                    state_scanner2 = False
                state_scanner3 = input('требуется ремонт ?(да/нет): ')
                if state_scanner3 == 'да':
                    state_scanner3 = True
                else:
                    state_scanner3 = False
                scan = input('(сканер)введите тип: ')
                scan2 = input('(сканер)введите название: ')
                scan3 = input('(сканер)введите колличество ')
                name_exm = Scanner(state_scanner, state_scanner2, state_scanner3, scan, scan2, int(scan3))
                if name_exm.is_old:
                    res['старая оргтехника'].setdefault(name_exm.name, []).append(name_exm.description_scanner())
                    res['старая оргтехника'][name_exm.name].append(name_exm.count)
                    with open(FILENAME, 'r+', encoding='utf-8') as file:
                        try:
                            data = json.load(file)
                            data['старая оргтехника'][name_exm.name] = [name_exm.description_scanner(), name_exm.count]
                            print(data)
                            with open(FILENAME, 'r+', encoding='utf-8') as file:
                                json.dump(data, file, ensure_ascii=False, indent=4)
                        except json.JSONDecodeError:
                            json.dump(res, file, ensure_ascii=False, indent=4)
                elif name_exm.new:
                    res['новая оргтехника'].setdefault(name_exm.name, []).append(name_exm.description_scanner())
                    res['новая оргтехника'][name_exm.name].append(name_exm.count)
                    with open(FILENAME, 'r+', encoding='utf-8') as file:
                        try:
                            data = json.load(file)
                            data['новая оргтехника'][name_exm.name] = [name_exm.description_scanner(), name_exm.count]
                            print(data)
                            with open(FILENAME, 'r+', encoding='utf-8') as file:
                                json.dump(data, file, ensure_ascii=False, indent=4)
                        except json.JSONDecodeError:
                            json.dump(res, file, ensure_ascii=False, indent=4)
                elif name_exm.repair:
                    res['требуется ремонт'].setdefault(name_exm.name, []).append(name_exm.description_scanner())
                    res['требуется ремонт'][name_exm.name].append(name_exm.count)
                    with open(FILENAME, 'r+', encoding='utf-8') as file:
                        try:
                            data = json.load(file)
                            data['требуется ремонт'][name_exm.name] = [name_exm.description_scanner(), name_exm.count]
                            print(data)
                            with open(FILENAME, 'r+', encoding='utf-8') as file:
                                json.dump(data, file, ensure_ascii=False, indent=4)
                        except json.JSONDecodeError:
                            json.dump(res, file, ensure_ascii=False, indent=4)


        else:
            if choose == 'списать':
                try:
                    take_count = input('введите количество которое хотите списать: ')
                    state_officeequipment = input('выбирите ветку хранения оргтехники: ')
                    name_officeequipmen = input('введите название оргтехники: ')
                    with open(FILENAME, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        count_officeequipmen = data[state_officeequipment][name_officeequipmen][1]
                        new_values = int(count_officeequipmen) - int(take_count)
                        if int(take_count) > count_officeequipmen:
                            raise SubErr(take_count, count_officeequipmen)
                        elif new_values == 0:
                            del data[state_officeequipment][name_officeequipmen]
                            with open(FILENAME, 'w+', encoding='utf-8') as f:
                                json.dump(data, f, ensure_ascii=False, indent=4)
                                print(data)
                        else:
                            data[state_officeequipment][name_officeequipmen] = [
                                data[state_officeequipment][name_officeequipmen][0], new_values]
                            with open(FILENAME, 'w+', encoding='utf-8') as f:
                                json.dump(data, f, ensure_ascii=False, indent=4)
                                print(data)
                except SubErr as er:
                    print(f'{er}')
                except ValueError as er2:
                    print(f'{er2}, введите число')
                except KeyError as er3:
                    print(f'{er3}: нет такой позиции на складе, введите правильное название')

            elif choose == 'q':
                quit()
