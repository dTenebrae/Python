# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.
my_sum = 0
with open('nums.txt', 'w+') as f:
    f.write(input('Input numbers: '))
    f.seek(0)
    for num in f.read().split():
        my_sum += int(num)
print(my_sum)
