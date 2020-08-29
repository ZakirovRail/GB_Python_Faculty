"""
2)	Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше
предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
# import random
#
# original_list = []
#
# # создаем псевдослучайный список
# for i in range(10):
#     original_list.append((random.randint(1, 200)))
# print(original_list)
#
# new_list = []
#
# # перебираем список по индексам и значениям и сравниваем с предыдущим значением
# for index, value in enumerate(original_list):
#     if original_list[index] > original_list[index - 1]:
#         new_list.append(value)  # добавляем в список элемент, если он больше предыдущего
#     else:
#         continue
#
# # выводим на печать со второго значения, поскольку в выборку может попасть 1-ое число,
# # которое больше самого последнего числа
# print(new_list[1:])


#Solution form teacher

my_list = [1, 9, 1, 72, 3, 4, 5, 6, 3]
new_list = [num for i, num in enumerate(my_list) if my_list[i] > my_list[i - 1] and i != 0]
print(new_list)
