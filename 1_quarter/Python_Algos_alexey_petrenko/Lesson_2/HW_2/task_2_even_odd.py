# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# number = str(input('Enter the number: '))
# list_digits = [i for i in number]
#
# print(number)
# print(list_digits)
#
# even_count = 0
# odd_count = 0
#
# for i in list_digits:
#     if int(i) % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#
# print(f'The number of even digits in the number you entered is {even_count}')
# print(f'The number of odd digits in the number you entered is {odd_count}')
# =====================================================================================================================
#  Solution from teacher

num = int(input('Enter number: '))
even, odd = 0, 0

while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
print(f'Even - {even}, Odd = {odd}')



