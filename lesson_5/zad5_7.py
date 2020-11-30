# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

profit_costs = {}
avg_profit = {'average_profit': 0}
counter = 0
with open('task_7.txt', 'r', encoding='UTF-8') as f:
    for items in f:
        name, form, proceeds, costs = items.split()
        proceeds = ''.join([lt for lt in proceeds if lt.isdigit()])
        costs = ''.join([lt for lt in costs if lt.isdigit()])
        profit_costs[name] = int(proceeds) - int(costs)
        if profit_costs.setdefault(name) >= 0:
            avg_profit['average_profit'] += int(profit_costs[name])
            counter += 1
avg_profit['average_profit'] = round((int(avg_profit['average_profit'])/counter), 2)
with open("data_file.json", "w") as write_file:
    json.dump((profit_costs, avg_profit), write_file)
