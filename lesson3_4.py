# Программа принимает действительное положительное число x и целое
# отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y). При решении
# задания необходимо обойтись без встроенной функции возведения числа в
# степень.


def my_func(var_x, var_y):
    inc_i = 2
    result = var_x
    while inc_i <= abs(var_y):
        result = result * var_x
        inc_i += 1
    return 1 / result


user_x = float(input('Введите действительное положительное число: '))
user_y = int(input('Введите целое отрицательное число: '))
print((lambda var_x, var_y: var_x ** var_y)(user_x, user_y))
print(my_func(user_x, user_y))
