"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

# number = input('Enter your number:')
#
# str_list_digits = ''.join(number)
# int_list_digits = []
#
# for i in str_list_digits:
#     int_list_digits.append(i)
#
# print(max(int_list_digits))

# Solution from teacher

num_user = int(input('Enter int: '))
current_max = 0
num = num_user  # отдельная переменная для хранения оставшейся части

while num > 0:
    digit = num % 10  # separate the last digit
    if digit > current_max:
        current_max = digit
        if current_max == 9: # Not nececary because anyway the max number is 9
            break
    num = num // 10  # separate from the number last digit

print('Max digit from enetered number is: ', current_max)





