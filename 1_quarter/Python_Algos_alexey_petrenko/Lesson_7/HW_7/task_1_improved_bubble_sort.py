import random

START = -100
STOP = 99
BASE = 10

arr = [random.randint(START, STOP) for i in range(BASE)]
print(f'original list is {arr}')


def reverse_bubble_sort(some_list):
    n = 1
    while n < len(some_list):
        for i in range(len(some_list) - 1):
            if some_list[i] < some_list[i + 1]:
                some_list[i + 1], some_list[i] = some_list[i], some_list[i + 1]
        n += 1


reverse_bubble_sort(arr)
print(f'Sorted list is {arr}')
