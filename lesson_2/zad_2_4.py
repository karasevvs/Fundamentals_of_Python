# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
user_input = input('Введите строку из нескольких слов, разделенных пробелами: ')
get_list = list(user_input.split(' '))
result = []
for i in range(len(get_list)):
    if len(get_list[i]) > 10:
        result.append(get_list[i][:10])
    else:
        result.append(get_list[i])
    print(f'{i+1}) {result[i]}')
