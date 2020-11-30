# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('my_file.txt', 'r', encoding='UTF-8') as f:
    for i, line in enumerate(f.readlines()):
        words = 0
        if len(line) > 2:  # слово это все, что больше 2х символов
            words = 1
            for ind, sym in enumerate(line):
                if sym == ' ':
                    words += 1
        print(f'{i+1} стр. - {words} слв.')
    print('-' * 25)
    print(f'Общее количество строк: {i + 1}')

