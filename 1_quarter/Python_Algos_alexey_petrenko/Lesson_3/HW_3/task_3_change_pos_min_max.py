import random

# LENGTH = 5
# START = 0
# STOP = 100
#
# random_list = [random.randint(START, STOP) for i in range(LENGTH)]
# print(random_list)
#
# max_num = 0
# min_num = random_list[0]
#
# for i in random_list:
#     if i > max_num:
#         max_num = i
#     if i < min_num:
#         min_num = i
#
# print(f'The max number is: {max_num}')
# print(f'The min number is: {min_num}')
# print(f'The index of max number is: {random_list.index(max_num)}')
# print(f'The index of min number is: {random_list.index(min_num)}')
# index_max = random_list.index(max_num)
# index_min = random_list.index(min_num)
# print(index_max)
# print(index_min)
#
# random_list[index_max], random_list[index_min] = random_list[index_min], random_list[index_max]
# print(random_list)

# COMMENT FOR ME - WRONG SOLUTION - there are some errors

# =====================================================================================================================
# Solution from teacher

N = 10
MIN_ITEM = -800
MAX_ITEM = 750
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(N)]
print(array)

# version 1
idx_min = 0
idx_max = 0

for i in range(len(array)):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i

array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)

# version 2

min_num = min(array)
max_num = max(array)
idx_min = array.index(min_num)
idx_max = array.index(max_num)
array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)
