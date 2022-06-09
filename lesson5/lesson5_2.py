# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


filename = input('Input filename: ')
with open(filename) as f:
    str_list = f.readlines()
for i, string in enumerate(str_list, 1):
    print(f'#{i}: Number of words: {len(string.split())}')
print(f'Number of lines: {len(str_list)}')
