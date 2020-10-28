# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

# number = input('Enter your number: ')
# new_number = [i for i in number]
# print(new_number)
# final_number = new_number[::-1]
# final_number = ''.join(final_number).strip('0')
# print(int(final_number))
# =====================================================================================================================
#  Solution from teacher
BASE = 10

num = int(input('Enter your number: '))
result = 0

while num > 0:
    result * BASE + num % BASE
    num = num //BASE

print(result)

# #  version 2 not for HW2
# num = int(input('Enter your number: '))
# result = ''
#
# for i in num:
#     result = i + result
# print(result)
#
#
# #  version 3 not for HW2
# num = int(input('Enter your number: '))
# result = num[::-1]
# print(result)

