import random

NUMBER = 15

or_list = [random.randint(1, 50) for i in range(NUMBER)]
print(or_list)


def selection_sort(arr):
    for i in range(len(arr)):
        idx_min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[idx_min]:
                idx_min = j
        arr[idx_min], arr[i] = arr[i], arr[idx_min]


test_arr = [25, 32, 10, 47, 50, 26, 46, 25, 29, 4, 45, 3, 24, 14, 5]
selection_sort(test_arr)
print(test_arr)
