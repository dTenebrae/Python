# Пользователь вводит целое положительное число. Найдите самую большую цифру
# в числе. Для решения используйте цикл while и арифметические операции.

user_int = int(input('Введите целое положительное число: '))
l_part = user_int % 10
f_part = user_int // 10
while f_part > 0:
    if f_part % 10 > l_part:
        l_part = f_part % 10
    f_part = f_part // 10
print(str(l_part))
