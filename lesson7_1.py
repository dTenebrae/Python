# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
# в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц). Результатом сложения
# должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix_list):
        self.matrix = matrix_list

    def __str__(self):
        result_output = ''
        for line in self.matrix:
            result_output += ''.join(str(line)) + '\n'
        return result_output

    def __add__(self, other):
        if (len(self.matrix[0]) != len(other.matrix[0])) \
                or len(self.matrix) != len(other.matrix):
            print('Have to be equal size matrices')
        else:
            result_matrix = []
            row = []
            for line in zip(self.matrix, other.matrix):
                for i, item in enumerate(line[0]):
                    row.append(item + line[1][i])
                result_matrix.append(row)
                row = []
            return result_matrix


mtx_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mtx_list2 = [[5, 9, 1], [8, 23, 7], [1, 1, 9]]

mtx1 = Matrix(mtx_list1)
mtx2 = Matrix(mtx_list2)
print(mtx1)
print(mtx2)
mtx3 = Matrix(mtx1 + mtx2)
print(mtx3)
