"""
1)	Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


# def devider(num1, num2):
#     try:
#         result = num1 / num2
#         return result
#     except ZeroDivisionError:
#         print('Second argument is zero. Please correct your number')

# print(devider(5, 0))
# Непонятно почему возвращает кроме сообщения еще и None

#-------------------------------------------------------------------------------
#Второй способ

# def devider(num1, num2):
#     if num2 != 0:
#         print(num1 / num2)
#     else:
#         print('Second argument is zero. Please correct your number')
#
# # print(devider(5, 0))
# print(devider(5, 3))


# Solution from teacher

def my_dev(num_1, num_2):
    try:
        num_1, num_2 = float(num_1), float(num_2)
        answer = num_1 / num_2
    except ValueError:
        return 'Error of number'
    except ZeroDivisionError:
        return 'Devision to zero'
    return answer
