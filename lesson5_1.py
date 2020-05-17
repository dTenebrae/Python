# Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных свидетельствует
# пустая строка.

with open('user_log.txt', 'w') as f:
    while True:
        user_str = input('Input string: ') + '\n'
        if user_str == '\n':
            break
        f.write(user_str)