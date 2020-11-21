or_list = [87, 84, 37, 95, 61, 19, 42, 19, 59, 60, 28, 76, 34, 22, 18, 52, 52, 63, 56, 13]


def bubble_sort(some_list):
    n = 1
    while n < len(some_list):
        for i in range(len(some_list) - 1):
            if some_list[i] > some_list[i + 1]:
                some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
        n += 1
    return some_list


print(bubble_sort(or_list))
