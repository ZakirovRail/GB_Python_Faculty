"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

# import random
#
# random_number = random.randint(1, 15)
# print(random_number)
# list_digits = []
# counter = 0
# while counter < random_number:
#     list_digits.append(random.randint(1, 150))
#     counter += 1
# print(list_digits)
#
# with open('file_5.txt', 'w', encoding='utf-8') as file:
#     for number in list_digits:
#         file.write(str(number))
#         file.write('\n')
#
# with open('file_5.txt', 'r', encoding='utf-8') as file_to_read:
#     sum_num = []
#     for line in file_to_read:
#         sum_num.append(int(line))
#     print('Сумма всех чисел в файле составляет {}: '.format(sum(sum_num)))

# Solution from teacher

with open('5.txt', 'w') as f:
    nums = input('Введите целые числа через пробел: ')
    f.write('Введенные числа: ', + nums + '\n')
    nums = map(int, nums.split())  # without list
    sum_nums = sum(nums)
    f.write('Сумма чисел: ' + str(sum_nums))
    print('Сумма введенных чисел: ', sum_nums)
print('Все записано в файл')
