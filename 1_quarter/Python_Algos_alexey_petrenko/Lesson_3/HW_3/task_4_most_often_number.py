import random

# LENGTH = 10
# START = 1
# STOP = 6
#
# list_numbers = [random.randint(START, STOP) for x in range(LENGTH)]
# print(list_numbers)
# dict_numbers = {}
#
# for i in list_numbers:
#     if i not in dict_numbers:
#         dict_numbers[i] = 1
#
#     elif i in dict_numbers:
#         dict_numbers[i] += 1
# print(dict_numbers)
#
# values = dict_numbers.values()
# print(values)
# =====================================================================================================================
# Solution from teacher

SIZE = 10
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, SIZE // 1.5) for _ in range(SIZE)]
print(array)

# version 1

num = array[0]
frequency = 1
for i in range(len(array)):
    spam = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            spam += 1
    if spam > frequency:
        frequency = spam
        num = array[i]

print(f'Число {num} встречается {frequency} раз(а)' if frequency > 1 else 'Все элементы уникальны')

# version 2
counter = {}
frequency = 1
num = None

for item in array:
    if item in counter:
        counter[item] += 1
    else:
        counter[item] = 1
    if counter[item] > frequency:
        frequency = counter[item]
        num = item
if num is not None:
    print(f'Число {num} встречается {frequency} раз(а)')
else:
    print('Все элементы уникальны')
