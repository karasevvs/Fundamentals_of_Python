# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(p_1, p_2, p_3):
    try:
        str_1 = [int(p_1), int(p_2), int(p_3)]
        str_1 = sorted(str_1, reverse=True)
        sum_max = str_1[0] + str_1[1]
        return print(f'Ответ: {sum_max}')
    except ValueError:
        print('Ошибка, только целые числа!')


try:
    a, b, c = input('Введите 3 числа через пробел: ').split()
    my_func(a, b, c)
except ValueError:
    print('УПС, введите все данные')

