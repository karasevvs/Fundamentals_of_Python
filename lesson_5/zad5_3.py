# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
def create_user():
    get_user = None
    while get_user != 'q':
        get_user = input('Введите фамилию сотрудника и величину оклада через пробел: ')
        if get_user != 'q':
            with open('users.txt', 'a', encoding='UTF-8') as f:
                f.write('\n' + get_user)


def calculate():
    salary_min = []
    salary_sum = []
    with open('users.txt', 'r', encoding='UTF-8') as f:
        list_1 = f.read().split('\n')
        for lt in range(1, len(list_1)):
            item = list_1[lt].split()
            if int(item[1]) < 20000:
                salary_min.append(item[0])
            salary_sum.append(item[1])
    print(f'Список сотрудников с зп < 20.000: \n{salary_min}')
    print('-' * 33)
    result = sum(map(int, salary_sum)) / len(salary_sum)
    print(f'Средний доход сотрудников составляет: {round(result, 3)}')


# -----------------------------------------------------------------------------
create_user()
calculate()
