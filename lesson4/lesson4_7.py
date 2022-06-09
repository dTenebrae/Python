# Реализовать генератор с помощью функции с ключевым словом yield, создающим
# очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n). Функция
# отвечает за получение факториала числа, а в цикле необходимо выводить только
# первые n чисел, начиная с 1! и до n!.


def my_factorial(n):
    count = 1
    fact = 1
    while count <= n:
        yield fact
        count += 1
        fact *= count


for num in my_factorial(5):
    print(num)