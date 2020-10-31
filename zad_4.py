# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = input('Введите целое положительное число: ')
i = 0
max_number = int(user_number[0])
while i < len(user_number):
    if int(user_number[i]) > max_number:
        max_number = int(user_number[i])
        i += 1
    else:
        i += 1
print(max_number)

# реализация через цикл for вышла короче
# max_number = int(user_number[0])
# for i in range(len(user_number)):
#     if int(user_number[i]) > max_number:
#         max_number = int(user_number[i])
# print(max_number)
