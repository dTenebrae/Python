# Создать вручную и заполнить несколькими строками текстовый файл, в котором
# каждая строка должна содержать данные о фирме: название, форма собственности,
# выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней
# прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их
# прибылями, а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка:
# [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json as js

firm_dict = dict()
avg_dict = dict()
f_sum = 0
result_list = []

with open('firm.txt') as raw_file:
    for item in raw_file.readlines():
        firm_dict[item.split()[0]] = int(item.split()[2]) - \
                                     int(item.split()[3])
result_list.append(firm_dict)
for value in firm_dict.values():
    f_sum += value
avg_dict['average_profit'] = f_sum / len(firm_dict)
result_list.append(avg_dict)

with open('firm.json', 'w') as result_file:
    js.dump(result_list, result_file)
