"""
3)	Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


# def my_func(arg1, arg2, arg3):
#     list_of_all_args = [arg1, arg2, arg3]
#     list_of_max = list()  # создаем пустой список для будущих максимальных чисел
#
#     # находим первое максимальное число и добавляем в список максимальных чисел
#     list_of_max.append(max(list_of_all_args))
#
#     # удаляем из общего списка первое максимальное число
#     list_of_all_args.remove(max(list_of_all_args))
#
#     # находим второе максимальное число из оставшихся двух и добавляем в список максимальных чисел
#     list_of_max.append(max(list_of_all_args))
#     print(list_of_max)  # убедимся что в списке максимальные только числа
#     print(sum(list_of_max))  # сумма максимальных числе
#
#
# my_func(10, 20, 30)
# my_func(0, 0, 0)
# my_func(-5, 0, 20)

#Slution from teacher

def my_func(num_1, num_2, num_3):
    try:
        my_list = [num_1, num_2, num_3]
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return 'Check number'

print(my_func(-5, 10, 0))