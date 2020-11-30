# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.
class My_error_value(Exception):
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    @staticmethod
    def deleting(number_1, number_2):
        try:
            return number_1 / number_2
        except ZeroDivisionError:
            return 'Деление на ноль'


print(My_error_value.deleting(1, 2))
