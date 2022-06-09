# Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше
# издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников
# фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if revenue > costs:
    print('Фирма приносит прибыль')
    profit = revenue - costs
    rent = profit / revenue * 100
    print('Рентабельность выручки: {:.2f}%'.format(rent))
    emp_number = int(input('Введите число сотрудников: '))
    proft_per_hmn = profit / emp_number
    print('Прибыль в расчете на одного сотрудника составляет: {:.2f}'
          .format(proft_per_hmn))
elif revenue < costs:
    print('Фирма приносит убытки')
else:
    print('Фирма работает в ноль')