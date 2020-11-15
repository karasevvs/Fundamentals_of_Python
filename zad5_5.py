# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

a = [randint(1, 100) for i in range(50)]
b = str(a).replace(', ', ' ')[1:-1]
with open('task_5.txt', 'w') as f:
    f.writelines(b)
print(f'СУММА из генератора: {sum(a)}')
with open('task_5.txt', 'r') as f:
    c = sum(map(int, f.read().split()))
print(f'СУММА из файла: {c}')

