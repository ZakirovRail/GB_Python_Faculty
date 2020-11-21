import random

START = 1
STOP = 100
NUMBER = 15

arr = [random.randint(START, STOP) for i in range(NUMBER)]
print(arr)


def insertion(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i
        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1
        array[j] = spam
        print(array)


insertion(arr)
print(arr)
