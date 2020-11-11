import random

# LENGTH = 15
# START = -101
# STOP = -1
#
# neg_list = [random.randint(START, STOP) for i in range(LENGTH)]
# print(neg_list)
#
# max_num = START
# min_num = int
#
# for i in neg_list:
#     if i > max_num:
#         max_num = i
#         # print(max_num)
# print(f'The max num in the list is: {max_num} and it is index is: {neg_list.index(max_num)}')
# =====================================================================================================================
# Solution from teacher

SIZE = 10
MIN_ITEM = -800
MAX_ITEM = -750
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# version 1

i = 0
index = -1

while i < len(array):
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array[i] > array[index]:
        index = i
    i += 1

if index != -1:
    print(f'Максимальное отрицательное число {array[index]}'
          f' находится в ячейке {index}')

# version 2

num = float('-inf')
for i, item in enumerate(array):
    if 0 > item > num:
        num = item
        index = 1

if num != float('-inf'):
    print(f'Максимальное отрицательное число {num}'
          f' находится в ячейке {index}')
