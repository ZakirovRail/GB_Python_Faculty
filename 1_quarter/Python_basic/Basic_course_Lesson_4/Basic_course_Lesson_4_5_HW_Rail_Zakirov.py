"""
5)	Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления
произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
# from functools import reduce
#
# my_list = [i for i in range(100, 1001) if i % 2 == 0]  # создаем список четных чисел
# print(my_list)
# final_list = reduce(lambda a, b: a * b, my_list)  # вычисляем произведение всех элементов списка
# print(final_list)


# Solution from teacher

from functools import reduce


def mul_list(n1, n2):
    return n1 * n2


my_list = [x for x in range(100, 1001) if x % 2 == 0]
reduce(mul_list, my_list)
