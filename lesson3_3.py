# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов


def my_func(var_1, var_2, var_3):
    list_a = [int(var_1), int(var_2), int(var_3)]
    return sorted(list_a, reverse=True)[0] + sorted(list_a, reverse=True)[1]


print(my_func(3, 8, 5))
