"""
3)	Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""

# list_numbers = [i for i in range(20, 240) if (i % 20 == 0 or i % 21 == 0)]
# print(list_numbers)


# Solution from teacher
print([x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0])
