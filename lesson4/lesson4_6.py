# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle

evens = count(3, 2)
print([next(evens) for _ in range(30)])

cycle_a = cycle('ksjfbksvdkjbgfkdjbg')
print([next(cycle_a) for _ in range(10)])