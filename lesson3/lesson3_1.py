# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.


def my_division(upper_digit, bottom_digit):
    try:
        result = upper_digit / bottom_digit
        return result
    except ZeroDivisionError:
        print('Деление на ноль!')
        result = float('inf') if upper_digit >= 0 else float('-inf')
        return result


while True:
    digit_list = input('Введите два числа через пробел: ').split()
    if len(digit_list) == 2:
        break
    print('Некорректный ввод!')
print(f'Результат деления: '
      f'{my_division(int(digit_list[0]), int(digit_list[1])):.2f}')
