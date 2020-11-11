import random

# LENGTH = 10
# START = 1
# STOP = 101
#
# rand = [random.randint(START, STOP) for x in range(LENGTH)]
# print(rand)
# ind_list = []
#
# for num in rand:
#     if num % 2 == 0:
#         ind_list.append(rand.index(num))
#
# print(ind_list)
# =====================================================================================================================
# Solution from teacher

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

result = []

for i in range(len(array)):
    if array[i] % 2 == 0:
        result.append(i)
print(f'Индексы четных элементов: {result}')

result_new = [i for i in range(len(array)) if array[i] % 2 == 0]
print(f'Индексы четных элементов: {result_new}')
