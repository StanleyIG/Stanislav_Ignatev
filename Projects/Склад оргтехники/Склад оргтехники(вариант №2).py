import json
from enum import Enum


class Officeequipment:
    def __init__(self, state, brand):  # состояние, тип оргтехники
        self.state = state
        self.brand = brand


class Printer(Officeequipment):
    def __init__(self, state, brand, name, count):
        super().__init__(state, brand)
        self.name = name
        self.count = count

    def description_printer(self):
        return f'брэнд {self.brand}, модель: {self.name}, состояние: {self.state}.'


class Scanner(Officeequipment):
    def __init__(self, state, brand, name, count):  # название, габариты, состояние
        super().__init__(state, brand)
        self.name = name
        self.count = count

    def description_scanner(self):
        return f'брэнд {self.brand}, модель: {self.name}, состояние: {self.state}.'


class Copier(Officeequipment):
    def __init__(self, state, brand, name, count):
        # состояние, тип, название, габариты, колличество
        super().__init__(state, brand)
        self.name = name
        self.count = count

    def description_copier(self):
        return f'брэнд {self.brand}, модель: {self.name}, состояние: {self.state}.'


class SubErr(Exception):
    def __init__(self, data, data2):
        self.data = data
        self.data2 = data2

    def __str__(self):
        return f'запрашиваемое колличество {self.data}, на складе:{self.data2}'


class StateErr(Exception):
    def __init__(self, state):
        self.state = state

    def __str__(self):
        return f' неверное значение: {self.state}, правильно введите одно из трёх состояний (старая/новая/ремонт)'


class OfficeEquipmenWarehouse:
    FILENAME = 'OfficeEquipmenWarehouse.json'
    res = {'старая оргтехника': {},
           'новая оргтехника': {},
           'нужен ремонт': {}}

    while True:
        choose = input('добавить/списать(нажмите "q" чтобы выйти): ')
        if choose == 'добавить':
            try:
                choose2 = input('выбирите тип оргтехники(ксерокс, принтер, сканер): ')
                if choose2 == 'ксерокс':
                    name_exm = '1'
                    name_exm += name_exm
                    cop = input('(ксерокс)введите тип: ')
                    cop2 = input('(ксерокс)введите название: ')
                    cop3 = input('(ксерокс)введите колличество ')
                    state = input('выбирите одно из 3-х состояний(старая/новая/ремонт: ')
                    name_exm = Copier(state, cop, cop2, int(cop3))
                    if name_exm.state == 'старая':
                        res['старая оргтехника'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                        res['старая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.description_copier())
                        res['старая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.count)
                        with open(FILENAME, 'r+', encoding='utf-8') as file:
                            try:
                                data = json.load(file)
                                data['старая оргтехника'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                                data['старая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.description_copier())
                                data['старая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.count)
                                print(data)
                                with open(FILENAME, 'r+', encoding='utf-8') as file:
                                    json.dump(data, file, ensure_ascii=False, indent=4)
                            except json.JSONDecodeError:
                                json.dump(res, file, ensure_ascii=False, indent=4)
                    elif name_exm.state == 'новая':
                        res['новая оргтехника'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                        res['новая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.description_copier())
                        res['новая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.count)
                        with open(FILENAME, 'r+', encoding='utf-8') as file2:
                            try:
                                data = json.load(file2)
                                data['новая оргтехника'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                                data['новая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.description_copier())
                                data['новая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.count)
                                print(data)
                                with open(FILENAME, 'r+', encoding='utf-8') as file2:
                                    json.dump(data, file2, ensure_ascii=False, indent=4)
                            except json.JSONDecodeError:
                                json.dump(res, file2, ensure_ascii=False, indent=4)
                    elif name_exm.state == 'ремонт':
                        res['требуется ремонт'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                        res['требуется ремонт'][name_exm.brand][name_exm.name].append(name_exm.description_copier())
                        res['требуется ремонт'][name_exm.brand][name_exm.name].append(name_exm.count)
                        with open(FILENAME, 'r+', encoding='utf-8') as file3:
                            try:
                                data = json.load(file3)
                                data['требуется ремонт'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                                data['требуется ремонт'][name_exm.brand][name_exm.name].append(name_exm.description_copier())
                                data['требуется ремонт'][name_exm.brand][name_exm.name].append(name_exm.count)
                                print(data)
                                with open(FILENAME, 'r+', encoding='utf-8') as file3:
                                    json.dump(data, file3, ensure_ascii=False, indent=4)
                            except json.JSONDecodeError:
                                json.dump(res, file3, ensure_ascii=False, indent=4)
                    else:
                        raise StateErr(state)

                elif choose2 == 'принтер':
                    name_exm = '2'
                    name_exm += name_exm
                    pr = input('(принтер)введите тип: ')
                    pr2 = input('(принтер)введите название: ')
                    pr3 = input('(принтер)введите колличество ')
                    state = input('выбирите одно из 3-х состояний(старая/новая/ремонт: ')
                    name_exm = Printer(state, pr, pr2, int(pr3))
                    if name_exm.state == 'старая':
                        res['старая оргтехника'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                        res['старая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.description_printer())
                        res['старая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.count)
                        with open(FILENAME, 'r+', encoding='utf-8') as file:
                            try:
                                data = json.load(file)
                                data['старая оргтехника'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                                data['старая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.description_printer())
                                data['старая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.count)
                                print(data)
                                with open(FILENAME, 'r+', encoding='utf-8') as file:
                                    json.dump(data, file, ensure_ascii=False, indent=4)
                            except json.JSONDecodeError:
                                json.dump(res, file, ensure_ascii=False, indent=4)
                    elif name_exm.state == 'новая':
                        res['новая оргтехника'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                        res['новая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.description_printer())
                        res['новая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.count)
                        with open(FILENAME, 'r+', encoding='utf-8') as file:
                            try:
                                data = json.load(file)
                                data['новая оргтехника'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                                data['новая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.description_printer())
                                data['новая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.count)
                                print(data)
                                with open(FILENAME, 'r+', encoding='utf-8') as file:
                                    json.dump(data, file, ensure_ascii=False, indent=4)
                            except json.JSONDecodeError:
                                json.dump(res, file, ensure_ascii=False, indent=4)
                    elif name_exm.state == 'старая':
                        res['требуется ремонт'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                        res['требуется ремонт'][name_exm.brand][name_exm.name].append(name_exm.description_printer())
                        res['требуется ремонт'][name_exm.brand][name_exm.name].append(name_exm.count)
                        with open(FILENAME, 'r+', encoding='utf-8') as file:
                            try:
                                data = json.load(file)
                                data['требуется ремонт'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                                data['требуется ремонт'][name_exm.brand][name_exm.name].append(name_exm.description_printer())
                                data['требуется ремонт'][name_exm.brand][name_exm.name].append(name_exm.count)
                                print(data)
                                with open(FILENAME, 'r+', encoding='utf-8') as file:
                                    json.dump(data, file, ensure_ascii=False, indent=4)
                            except json.JSONDecodeError:
                                json.dump(res, file, ensure_ascii=False, indent=4)
                    else:
                        raise StateErr(state)

                elif choose2 == 'сканер':
                    name_exm = '3'
                    name_exm += name_exm
                    scan = input('(сканер)введите тип: ')
                    scan2 = input('(сканер)введите название: ')
                    scan3 = input('(сканер)введите колличество ')
                    state = input('выбирите одно из 3-х состояний(старая/новая/ремонт: ')
                    name_exm = Scanner(state, scan, scan2, int(scan3))
                    if name_exm.state == 'старая':
                        res['старая оргтехника'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                        res['старая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.description_scanner())
                        res['старая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.count)
                        with open(FILENAME, 'r+', encoding='utf-8') as file:
                            try:
                                data = json.load(file)
                                data['старая оргтехника'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                                data['старая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.description_scanner())
                                data['старая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.count)
                                print(data)
                                with open(FILENAME, 'r+', encoding='utf-8') as file:
                                    json.dump(data, file, ensure_ascii=False, indent=4)
                            except json.JSONDecodeError:
                                json.dump(res, file, ensure_ascii=False, indent=4)
                    elif name_exm.state == 'новая':
                        res['новая оргтехника'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                        res['новая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.description_scanner())
                        res['новая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.count)
                        with open(FILENAME, 'r+', encoding='utf-8') as file:
                            try:
                                data = json.load(file)
                                data['новая оргтехника'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                                data['новая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.description_scanner())
                                data['новая оргтехника'][name_exm.brand][name_exm.name].append(name_exm.count)
                                print(data)
                                with open(FILENAME, 'r+', encoding='utf-8') as file:
                                    json.dump(data, file, ensure_ascii=False, indent=4)
                            except json.JSONDecodeError:
                                json.dump(res, file, ensure_ascii=False, indent=4)
                    elif name_exm.state == 'ремонт':
                        res['требуется ремонт'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                        res['требуется ремонт'][name_exm.brand][name_exm.name].append(name_exm.description_scanner())
                        res['требуется ремонт'][name_exm.brand][name_exm.name].append(name_exm.count)
                        with open(FILENAME, 'r+', encoding='utf-8') as file:
                            try:
                                data = json.load(file)
                                data['требуется ремонт'].setdefault(name_exm.brand, {}).setdefault(name_exm.name, [])
                                data['требуется ремонт'][name_exm.brand][name_exm.name].append(name_exm.description_scanner())
                                data['требуется ремонт'][name_exm.brand][name_exm.name].append(name_exm.count)
                                print(data)
                                with open(FILENAME, 'r+', encoding='utf-8') as file:
                                    json.dump(data, file, ensure_ascii=False, indent=4)
                            except json.JSONDecodeError:
                                json.dump(res, file, ensure_ascii=False, indent=4)
                    else:
                        raise StateErr(state)

            except StateErr as err:
                print(f'{err}')
            except ValueError as err2:
                print(f'{err2}, введите целое число')

        else:
            if choose == 'списать':
                try:
                    take_count = input('введите количество которое хотите списать: ')
                    state_officeequipment = input('выбирите ветку хранения оргтехники: ')
                    brand_officeequipmen = input('введите брэнд оргтехники: ')
                    name_officeequipmen = input('введите модель оргтехники: ')
                    with open(FILENAME, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        count_officeequipmen = data[state_officeequipment][brand_officeequipmen][name_officeequipmen][1]
                        new_values = int(count_officeequipmen) - int(take_count)
                        if int(take_count) > count_officeequipmen:
                            raise SubErr(take_count, count_officeequipmen)
                        elif new_values == 0:
                            del data[state_officeequipment][brand_officeequipmen][name_officeequipmen]
                            with open(FILENAME, 'w+', encoding='utf-8') as f:
                                json.dump(data, f, ensure_ascii=False, indent=4)
                                print(data)
                        else:
                            data[state_officeequipment][brand_officeequipmen][name_officeequipmen] = [
                                data[state_officeequipment][brand_officeequipmen][name_officeequipmen][0], new_values]
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


