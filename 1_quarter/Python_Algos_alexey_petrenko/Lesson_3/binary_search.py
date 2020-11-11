import random

SIZE = 1000
MIN_VAL = 0
MAX_VAL = 100000

array = [random.randint(MIN_VAL, MAX_VAL) for _ in range(SIZE)]
array.sort()  # binary search works only for sorted list
print(array)

find = int(input('Enter you number to find: '))
pos = len(array) // 2
left = 0
right = len(array) - 1
count = 1

while find != array[pos] and left <= right:
    count += 1
    if find > array[pos]:
        left = pos + 1
    elif find < array[pos]:
        right = pos - 1
    pos = (left + right) // 2

print('The element is absent' if left > right else f'Element has position {pos}')
print(f'{count}')
