from collections import deque

BASE = 16

HEX_NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F')

BIN_NUMBERS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def sum_hex(first, second):
    first = first.copy()
    second = second.copy

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    result = deque()
    overflow = 0
    while len(first) != 0:
        first_num = BIN_NUMBERS[first.pop()]
        second_num = BIN_NUMBERS[second.pop()]

        result_num = first_num + second_num + overflow

        if result_num >= BASE:
            overflow = 1
            result_num -= BASE
        else:
            overflow = 0

        result.appendleft(HEX_NUMBERS[result_num])

    if overflow == 1:
        result.appendleft('1')

    return result


def mult_hex(first, second):
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))
    result = deque('0')

    while len(second) != 0:
        second_num = BIN_NUMBERS[second.pop()]

        spam = deque('0')
        for _ in range(second_num):
            spam = sum_hex(spam, first)

        spam.extend('0' * (len(first) - len(second) - 1))
        result = sum_hex(result, spam)

    return result


a = deque(input('Enter first number in hex format: ').upper())
b = deque(input('Enter second number in hex format: ').upper())

# z = hex(int('a2', 16) + int('c4f', 16)) # bad example

print(f'{list(a)} + {list(b)} = {list(sum_hex(a, b))}')
print(f'{a} + {b} = {mult_hex(a, b)}')
