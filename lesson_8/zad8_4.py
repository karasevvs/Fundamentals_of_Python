# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
class Store:

    def __init__(self, name, price, counter):
        self.name = name
        self.price = price
        self.counter = counter
        self.full = []
        self.current = []
        self.list = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.counter}

    def __str__(self):
        return f'Имя: {self.name} Цена: {self.price} Количество: {self.counter}'

    def reception(self):
        try:
            name_1 = input(f'Введите наименование ')
            price_1 = int(input(f'Введите цену за ед '))
            counter_1 = int(input(f'Введите количество '))
            unique = {'Модель устройства': name_1, 'Цена за ед': price_1, 'Количество': counter_1}
            self.list.update(unique)
            self.current.append(self.list)
        except ValueError:
            return f'Ошибка ввода данных'

        print(f'Чтобы выйти "q"')
        if input('') == 'q':
            self.full.append(self.current)
            return f'Общий склад:\n {self.full}'
        else:
            return Store.reception(self)


class Printer(Store):
    def the_printer(self, typing):
        self.list['Тип'] = typing
        return f'Список принтеров:\n{self.list}'


class Scanner(Store):
    def the_scanner(self, sizing):
        self.list['Разрешение'] = sizing
        return f'Список сканеров:\n{self.list}'


class Xerox(Store):
    def the_xerox(self, adding):
        self.list['Прочее'] = adding
        return f'Список ксероксов:\n{self.list}'


test_1 = Printer('HP', 26990, 100)
test_2 = Xerox('Xerox', 116990, 5)
test_3 = Scanner('Kyocera', 25000, 3)
print(test_1.reception())
print(test_2.reception())
print(test_3.reception())
print()
print(Printer.the_printer(test_1, 'A4'))
print()
print(Xerox.the_xerox(test_2, 'Уникальные данные'))
print()
print(Scanner.the_scanner(test_3, 300))
