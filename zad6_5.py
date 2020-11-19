# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        return print(f'Запуск отрисовки.\nИспользуем ручку\nТекст: {self.title}')


class Pencil(Stationery):
    def draw(self):
        return print(f'Запуск отрисовки.\nИспользуем карандаш\nТекст: {self.title}')


class Handle(Stationery):
    def draw(self):
        return print(f'Запуск отрисовки.\nИспользуем маркер\nТекст: {self.title}')


p_1 = Pen('какой-то красивый текст')
p_1.draw()
print('-' * 100)
p_2 = Pencil('какой-то текст')
p_2.draw()
print('-' * 100)
p_3 = Handle('текст')
p_3.draw()
