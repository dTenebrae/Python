# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например,
# пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_int = input('Введите целое число: ')
print(str(int(user_int) + int(user_int * 2) + int(user_int * 3)))