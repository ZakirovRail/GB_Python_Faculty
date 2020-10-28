#1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак
# операции вводятся пользователем.
# После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться
# при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю о
# невозможности деления на ноль, если он ввел его в качестве делителя.

# repeat_sign = ('+', '-', '*', '/')
#
# while True:
#     print('Enter two numbers and an operation. If you enter 0 instead of operation, the program closed')
#     first_num = int(input('first number:'))
#     second_num = int(input('second number:'))
#     operation = str(input('operation (+, -, * or /)'))
#
#     if operation == '0':
#         print('The program is closed')
#         break
#     else:
#         if operation == '+':
#             print(f'The sum of two numbers is: {first_num + second_num}')
#         if operation == '-':
#             print(f'The subtraction of two numbers is: {first_num - second_num}')
#         if operation == '*':
#             print(f'The multiplication of two numbers is: {first_num * second_num}')
#         if operation == '/' and second_num == 0:
#             print('Division 0 error. Try again')
#         if operation == '/' and second_num != 0:
#             print(f'The division of two numbers is: {first_num / second_num}')
# =====================================================================================================================
#  Solution from teacher
while True:
    sign = input("The sign (+, -, * , /):")
    if sign == '0':
        break
    if sign in {'+', '-', '*', '/'}:
        x = float(input('Enter the x = :'))
        y = float(input('Enter the y = :'))
        if sign == '+':
            print(f'{x + y:.2f}')
        elif sign == '-':
            print(f'{x - y:.2f}')
        elif sign == '*':
            print(f'{x * y:.2f}')
        elif y != 0:
            print(f'{x / y:.2f}')
        else:
            print('Division zero')
    else:
        print('Wrong sign of operation')