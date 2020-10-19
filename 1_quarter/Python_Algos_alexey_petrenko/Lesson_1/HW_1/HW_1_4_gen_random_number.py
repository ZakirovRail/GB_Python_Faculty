# Написать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

print('random number')
num_start = int(input('Beginning of a range: '))
num_end = int(input('End of a range: '))
result = random.randint(num_start, num_end)
print(result)

print('real number')
num_start = float(input('Beginning of a range: '))
num_end = float(input('End of a range: '))
result = random.uniform(num_start, num_end)
print(round(result, 3))

print('Random symbol')
num_start = ord(input('Beginning of a range: '))
num_end = ord(input('End of a range: '))
result = random.randint(num_start, num_end)
print(round(result, 3))

