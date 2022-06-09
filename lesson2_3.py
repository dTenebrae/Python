# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к
# какому времени года относится месяц (зима, весна, лето, осень). Напишите
# решения через list и через dict.
month_list = [['Январь', 'Зима'], ['Февраль', 'Зима'], ['Март', 'Весна'],
              ['Апрель', 'Весна'], ['Май', 'Весна'], ['Июнь', 'Лето'],
              ['Июль', 'Лето'], ['Август', 'Лето'], ['Сентябрь', 'Осень'],
              ['Октябрь', 'Осень'], ['Ноябрь', 'Осень'], ['Декабрь', 'Зима']]
month_dict = {1: month_list[0], 2: month_list[1], 3: month_list[2],
              4: month_list[3], 5: month_list[4], 6: month_list[5],
              7: month_list[6], 8: month_list[7], 9: month_list[8],
              10: month_list[9], 11: month_list[10], 12: month_list[11]}
while True:
    try:
        month = int(input('Введите номер месяца(1...12): '))
        break
    except ValueError:
        print('Введите целое число от 1 до 12!')
if month > 12:
    print('Вы ввели число, превышающее количество месяцев в году. '
          'Показываем ближайший к нему месяц')
    month = 12
if month < 1:
    print('Вы ввели число, меньше количества месяцев в году. '
          'Показываем ближайший к нему месяц')
    month = 1
# Через list
print(f'Месяц: {month_list[month-1][0]}, '
      f'Время года: {month_list[month-1][1]}')

# Через Dict
print(f'Месяц: {month_dict.get(month)[0]}, '
      f'Время года: {month_dict.get(month)[1]}')