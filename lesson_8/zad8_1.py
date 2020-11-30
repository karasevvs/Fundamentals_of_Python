# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Data:
    def __init__(self, str_1):
        self.str_1 = str(str_1)

    def __str__(self):
        return f'Дата: {Data.method_1(self.str_1)}'

    @classmethod
    def method_1(cls, str_1):
        full_date = []
        for i in str_1.split('-'):
            full_date.append(i)
        return int(full_date[0]), int(full_date[1]), int(full_date[2])

    @staticmethod
    def method_2(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 1 <= year <= 3000:
                    return 'Все верно'
                else:
                    return 'Ошибка - год'
            else:
                return 'Ошибка - месяц'
        else:
            return 'Ошибка - день'


print(Data('24-11-2020'))
print(Data.method_2(12, 10, 2020))
print(Data.method_2(40, 10, 2020))
print(Data.method_2(12, 13, 2020))
print(Data.method_2(12, 10, -1))
