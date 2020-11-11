import random

SIZE = 1_000

MIN_ITEM = 0
MAX_ITEM = 999
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

array.sort()  # only for this task
print(array)

find = int(input('Enter your number: '))
pos = len(array) // 2
left = 0
right = len(array) - 1
count = 1

while array[pos] != find and left <= right:
    count += 1
    if find > array[pos]:
        left = pos + 1
        # pos = (left + right) // 2
    elif find < array[pos]:
        right = pos - 1
    pos = (left + right) // 2

print('The element is absent' if left > right else f'Element has a position {pos}')
print(f'{count}')
