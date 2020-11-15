# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий
# по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
dates = {}
with open('task6_res.txt', 'r', encoding='UTF-8') as f:
    for items in f:
        name, lessons, practice, laboratory = items.split()
        lessons = (''.join(lt for lt in lessons if lt.isdigit()))
        practice = (''.join(lt for lt in practice if lt.isdigit()))
        laboratory = (''.join(lt for lt in laboratory if lt.isdigit()))
        if lessons == '':
            lessons = '0'
        if practice == '':
            practice = '0'
        if laboratory == '':
            laboratory = '0'
        dates[name] = str(sum(map(int, (lessons, practice, laboratory))))
print('-' * 100)
print(dates)
