"""
1)	Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""

our_list = []

our_list.append(123)
our_list.append({'key_1': 'value_1','key_2': 'value_2' })
our_list.append('stringtype')
our_list.append(bool(1))
our_list.append(set())
our_list.append(tuple())
# print(our_list)

for data_type in our_list:
    print(type(data_type))



