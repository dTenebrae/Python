# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

listA = []
while True:
    list_value = input(
        'Введите элемент списка. Если хотите выйти из режима '
        'ввода - введите ":q" --->')
    if list_value == ':q':
        break
    listA.append(list_value)
print(f'Список: {listA} Длина списка: {len(listA)}')
num = 0
if len(listA) % 2 == 0:
    max_len = len(listA)
else:
    max_len = len(listA) - 1
while num < max_len:
    listA[num], listA[num + 1] = listA[num + 1], listA[num]
    num += 2
print(f'Список: {listA} Длина списка: {len(listA)}')
