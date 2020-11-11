# list_numbers = [i for i in range(2, 100)]
# print(list_numbers)
# dict_digits = {i: 0 for i in range(2, 10)}
# print(dict_digits)
#
# for x in list_numbers:
#     for key, value in dict_digits.items():
#         if x % key == 0:
#             dict_digits[key] += 1
#
#
# for key, value in dict_digits.items():
#     print(f'Числу {key} кратно : {value} чисел ')


# =====================================================================================================================
# Solution from teacher

# Version 1

START_NUM = 2
END_NUM = 99
START_DIV = 2
END_DIV = 9

for i in range(START_DIV, END_DIV + 1):
    frequency = 0
    for j in range(START_NUM, END_NUM + 1):
        if j % i == 0:
            frequency += 1
    print(f'Число {i} кратно {frequency} чисел')

# Version 2
frequency = [0] * (END_DIV - START_DIV + 1)
for i in range(START_NUM, END_NUM + 1):
    for j in range(START_DIV, END_DIV + 1):
        if i % j == 0:
            frequency[j - START_DIV] += 1

for i, item in enumerate(frequency, start=START_DIV):
    print(f'Числу {i} кратно {item} чисел')
