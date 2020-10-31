# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
per_int = 1
per_float = 1.25
per_bool = True
per_list = ['один', '2.25', '3']
per_str = 'какой-то текст'
per_dist = {'1': 'январь', '2': 'февраль', '3': 'март'}
per_cort = ('test', 'ok', 'number', '123', '1.24')
print(f'Целое: {per_int} || C плав.точкой: {per_float} || Булевы: {per_bool} \n'
      f'Список: {per_list} || Строка: {per_str} || Словарь: {per_dist} \n'
      f'Кортеж: {per_cort}')

user_input = input("Введите число: ")
user_input_2 = input("Введите строку: ")
user_input_3 = input("Введите число с плав. точкой: ")
print('1) Получено число: {} с типом: {}'.format(user_input, type(user_input_2)))
print('2) Получена строка: {}'.format(user_input_2))
print(f'3) Получена строка: {user_input_3}, затем конверт,в итоге тип: {type(float(user_input_3))}')

