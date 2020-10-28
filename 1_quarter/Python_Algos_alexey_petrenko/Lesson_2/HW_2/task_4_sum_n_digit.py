#  Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
#  Количество элементов (n) вводится с клавиатуры.

# def row_numbers(n):  #  WRONG
#     # n = int(input('Enter a "n" value: '))
#     counter = 0
#     summ = 0
#     base = 1
#
#     if n == 0:
#         print(f'The summ is {summ}')
#         return summ
#
#     if n != 0:
#         summ += (base / -2)
#         print(f'ELSE BLOCK - The summ is {summ}')
#         print(summ)
#         return f'{summ}, {row_numbers(n-1)}'
#
#
# row_numbers(4)
# =====================================================================================================================
#  Solution from teacher

n = int(input('Enter how many element to be summ: '))
item = 1
sum_ = 0

for _ in range(n):
    sum_ += item
    item /= -2
print(sum_)

#  version 2
# summa_2 = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
# print(summa_2)
