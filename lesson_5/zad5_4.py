# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
calendar = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', }
new_list = []
with open('text_task_4.txt', 'r', encoding='UTF-8') as f:
    for lt in f:
        lt = lt.split(' ', 1)
        new_list.append(calendar[lt[0]] + ' ' + lt[1])
with open('result_task4.txt', 'w', encoding='UTF-8') as f_2:
    f_2.writelines(new_list)
