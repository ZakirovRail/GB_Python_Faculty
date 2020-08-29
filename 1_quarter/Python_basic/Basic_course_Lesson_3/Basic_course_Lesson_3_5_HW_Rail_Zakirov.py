"""
5)	Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
ранее сумме и после этого завершить программу.
"""

# def sum_of_numbers():
#     while True:
#         list_for_sum = list()
#         list_numbers_from_user = (input('Введите несколько цифр через пробел, чтобы вывести их сумму: '))
#         print(list_numbers_from_user)
#         for i in list_numbers_from_user:
#             if list_numbers_from_user.endswith('!'):
#                 list_numbers_from_user = list_numbers_from_user[:-1]
#             else:
#                 list_for_sum.append(int(i))
#             # else:
#             #     print('Вы ввели вместе с цифрами недопустимый символ, повторите ввод: ')
#             print(sum(list_for_sum))
#
#
# sum_of_numbers()

#Solution from teacher

def summary():
    ex = False
    result = 0
    while ex == False:
        numbers = input('Enter numbers or q to exit: ').split()
        res_line = 0
        for num in numbers:
            if 'q' in num:
                ex = True
                break
            else:
                res_line += int(num)
        result += res_line
    print(result)
