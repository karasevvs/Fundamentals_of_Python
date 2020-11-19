# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, color, speed=0, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} движется')

    def stop(self):
        self.speed = 0
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Направление автомобиля {self.name} - {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} = {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.name} превышение скорости ({self.speed})')
        else:
            print(f'Автомобиль {self.name} скорость в норме ({self.speed})')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Автомобиль {self.name} превышение скорости ({self.speed})')
        else:
            print(f'Автомобиль {self.name} скорость в норме ({self.speed})')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


car_1 = TownCar('BMW i320', 'black', 120)
car_1.go()
car_1.show_speed()
car_1.turn('direct')
car_1.stop()
print('-' * 100)
car_2 = WorkCar('Renault Logan', 'black', 30)
car_2.go()
car_2.show_speed()
car_2.turn('left')
car_2.stop()
print('-' * 100)
car_3 = SportCar('BMW M5', 'yellow', 220)
car_3.go()
car_3.show_speed()
car_3.turn('direct')
car_3.stop()
print('-' * 100)
car_4 = PoliceCar('YAZ HUNTER', 'blue', 100, True)
car_4.go()
car_4.show_speed()
car_4.turn('right')
car_4.stop()
print('-' * 100)
