# Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
# сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

salary_dict = dict()
try:
    with open('salary.txt') as f:
        salary_list = f.readlines()
    for name in salary_list:
        salary_dict[name.strip().split()[0]] = float(name.strip().split()[1])
        if salary_dict[name.strip().split()[0]] < 20000:
            print(f'{name.strip().split()[0]}: '
                  f'{salary_dict[name.strip().split()[0]]}')
    print(f'Средний доход: {sum(salary_dict.values()) / len(salary_dict):.2f}')
except FileNotFoundError:
    print('Файл не найден')
