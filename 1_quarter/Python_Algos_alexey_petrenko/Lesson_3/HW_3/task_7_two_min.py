# =====================================================================================================================
# Solution from teacher

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


# version 1

min_first, min_second = (0, 1) if array[0] < array[1] else (1, 0)
# in details
# if array[0] < array[1]:
#     min_first = 0
#     min_second = 1
# else:
#     min_first = 1
#     min_second = 0

for i in range(2, len(array)):
    if array[i] < array[min_first]:
        spam = min_first
        min_first = i
        if array[spam] < array[min_second]:
            min_second = spam

    elif array[i] < array[min_second]:
        min_second = i

print(f'Число {array[min_first]} в ячейке {min_first}')
print(f'Число {array[min_second]} в ячейке {min_second}')


# version 2
# min_1 = min(array)
# array.remove(min_1)
# min_2 = min(array)
# print(min_1, min_2)
