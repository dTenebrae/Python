# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны заменяться на
# русские. Новый блок строк должен записываться в новый текстовый файл.

rus_nums = []
with open('numbers.txt') as read_file:
    num_list = read_file.readlines()
for num in num_list:
    if num.split()[0] == 'One':
        rus_nums.append('Один - 1\n')
    elif num.split()[0] == 'Two':
        rus_nums.append('Два - 2\n')
    elif num.split()[0] == 'Three':
        rus_nums.append('Три - 3\n')
    elif num.split()[0] == 'Four':
        rus_nums.append('Четыре - 4\n')
    elif num.split()[0] == 'Five':
        rus_nums.append('Пять - 5\n')
    elif num.split()[0] == 'Six':
        rus_nums.append('Шесть - 6\n')
    elif num.split()[0] == 'Seven':
        rus_nums.append('Семь - 7\n')
    elif num.split()[0] == 'Eight':
        rus_nums.append('Восемь - 8\n')
    elif num.split()[0] == 'Nine':
        rus_nums.append('Девять - 9\n')
    elif num.split()[0] == 'Ten':
        rus_nums.append('Десять - 10\n')
with open('rus_numbers.txt', 'w') as write_file:
    write_file.writelines(rus_nums)
