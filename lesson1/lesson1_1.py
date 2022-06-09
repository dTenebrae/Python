# Поработайте с переменными, создайте несколько, выведите на экран, запросите
# у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

tn_str = 'string'
tn_int = 12
tn_float = 3.6
tn_bool = True
tn_list = [2, 'abc', (1, 2)]
tn_tuple = (1, 2, 3)
tn_dict = {'filename': 'python.py', 'size': 150}
print('\n')
print(f'{tn_str} принадлежит к типу {type(tn_str)},\n'
      f'{tn_int} принадлежит к типу {type(tn_int)},\n'
      f'{tn_float} принадлежит к типу {type(tn_float)},\n'
      f'{tn_bool} принадлежит к типу {type(tn_bool)},\n'
      f'{tn_list} принадлежит к типу {type(tn_list)},\n'
      f'{tn_tuple} принадлежит к типу {type(tn_tuple)},\n'
      f'{tn_dict} принадлежит к типу {type(tn_dict)}')
print('\n' + '='*70 + '\n')
tn_str = input('Введите строку: ')
tn_int = int(input('Введите целое число: '))

print('Вы ввели %s %d' % (tn_str, tn_int))
