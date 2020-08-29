"""
3)	Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого)
деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух
клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


# class Cell:
#     def __init__(self, nucleus):
#         self.nucleus = nucleus
#
#     def __add__(self, other):
#         return self.nucleus + other.nucleus

# def __sub__(self, other):
#     if other.nucleus > self.nucleus:
#         print(self.nucleus - other.nucleus)
#         print('Похоже, что полученный результат в виде отрицательного числа не верен. '
#               'Проверьте еще раз вводимые данные')
# else:
#     print(self.nucleus - other.nucleus)

# def __mul__(self, other):
#     print(self.nucleus * other.nucleus)

# def __truediv__(self, other):
#     try:
#         print(self.nucleus / other.nucleus)
#     except ZeroDivisionError as e:
#         print('Произошла ошибка', e)
#         print('Похоже, что вы вводите второй аргумент равный 0. Проверьте еще раз - деление на 0 невозможно')


# example1 = Cell(12)
# example2 = Cell(20)
# print(example1.nucleus)
# print(example1 + example2)
# print(example1 - example2)
# print(example1 * example2)
# example3 = Cell(12)
# example4 = Cell(0)
# print(example3 / example4)

# Третье задание решено частично


# Solution from teacher


class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return self.nums

    def __add__(self, other):
        return 'Sum of cell is ' + str(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'Ячеек в первой клетке меньше или равно второй, вычитание невоможно'

    def __mul__(self, other):
        return 'Multiply of cells is ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Truediv of cells is ' + round(self.nums / other.nums)


cell_1 = Cell(10)
cell_2 = Cell(14)
print(cell_1 + cell_2)
print(cell_2.make_order(5))
