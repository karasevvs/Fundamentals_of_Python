# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

number = input('Введите количество элементов списка: ')
user_list = []
try:
    for get_input in range(int(number)):
        get_user = input(f'Введите элемент {get_input + 1} списка: ')
        user_list.append(get_user)
    lt = 0
    print(f'Исходный: {user_list}')
    if int(number) % 2 == 0:
        while lt < len(user_list):
            dop_list = user_list[lt]
            user_list[lt] = user_list[lt + 1]
            user_list[lt + 1] = dop_list
            lt += 2
    if int(number) % 2 != 0:
        while lt < len(user_list) - 1:
            dop_list = user_list[lt]
            user_list[lt] = user_list[lt + 1]
            user_list[lt + 1] = dop_list
            lt += 2
    print(f'Результат: {user_list}')
except ValueError:
    print('Ошибка ввода')
