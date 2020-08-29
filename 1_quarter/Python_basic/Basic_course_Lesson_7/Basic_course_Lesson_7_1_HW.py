"""
1)	Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
 который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31	22
37	43
51	86


3	5	32
2	4	6
-1	64	-8


3	5	8	3
8	3	7	1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""
# matrix_list_1 = [[31, 22, 15], [37, 43, 18], [51, 86, 26]]
# matrix_list_2 = [[31, 22, 15], [37, 43, 15], [51, 86, 15]]
# matrix_list_3 = [[3, 5, 8, 3], [8, 3, 7, 1]]
#
#
# class Matrix:
#     def __init__(self, mat_data):
#         self.mat_data = mat_data
#
#     def __add__(self, matrix_1, matrix_2):
#         result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#         for i in range(len(matrix_list_1)):
#             for j in range(len(matrix_list_1[0])):
#                 result[i][j] = matrix_list_1[i][j] + matrix_list_2[i][j]
#         for i in range(len(result)):
#             for j in range(len(result[i])):
#                 print("{:4d}".format(result[i][j]), end="")
#             print()
#
#     def __str__(self):
#         return str(self.mat_data)
#
#     def print_matrix_list(self):
#         for row in range(len(self.mat_data)):
#             for number in range(len(self.mat_data[row])):
#                 print('{:5d}'.format(self.mat_data[row][number]), end="")
#             print()
#
#
# mat_list_1 = Matrix(matrix_list_1)
# print(mat_list_1.print_matrix_list())  # вывод матрицы
# print(mat_list_1)  # вызов матрицы __str__
# mat_list_1.__add__(matrix_list_1, matrix_list_2)  # сложение двух матриц __add__



# Solution from teacher


class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in line]) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Problems with shape'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join([str(i) for i in summed_line]) + '\n'
        else:
            return 'Problems with shape'
        return answer


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])

print(matrix_1)
print()
print(matrix_1 + matrix_2)