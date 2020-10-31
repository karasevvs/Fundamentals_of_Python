# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
user_number = int(input('Введите целое число n: '))
get_str = str(user_number)
get_format = ''
result = 0
for i in range(user_number):
    get_format += get_str
    result += int(get_format)
print(f'ИТОГ: {result}')

