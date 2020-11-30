# 3. Создайте собственный класс-исключение, который должен проверять
# содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
class My_error_value(Exception):
    def __init__(self, text):
        self.txt = text


data = []
while True:
    try:
        value = input('Введите данные: ')
        if value == 'stop':
            print(f'Список: {data}')
            break
        if not value.isdigit():
            raise My_error_value(value)
        else:
            data.append(int(value))
            print(f'Текуший список: {data}')
    except My_error_value:
        print('Ошибка ввод только чисел')
