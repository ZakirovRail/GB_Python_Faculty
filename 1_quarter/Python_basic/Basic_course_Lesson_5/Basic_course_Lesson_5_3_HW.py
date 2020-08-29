"""
3)	Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32

"""
# dict_of_salary = {}
#
# # проходимся по файлу и вносим в словарь значения фамилия-зарплата
# with open('file_3.txt', 'r', encoding='utf-8') as f_file:
#     for line in f_file:
#         key, value = line.split()
#         dict_of_salary[key] = value
# # print(dict_of_salary)
#
# # проходим по словарю и вывыодим на печать ЗП каждого из сотрудников
# for key in dict_of_salary:
#     if float(dict_of_salary[key]) < 20000:
#         print(f'This employee "{key}" has the amount of income less than 20000 \n')
#
#
# # вычисляем среднюю зарплату по всем сотрудникам
# counter = 0
# total_salary = 0
#
# for key in dict_of_salary:
#     # print(dict_of_salary[key])
#     counter += 1
#     total_salary += (float(dict_of_salary[key]))
#     average_salary = total_salary / counter
# print(f'The average salary of all employees is {average_salary}')

# Solution from teacher
"""
Имя1 - 20000
Имя2 - 30000
"""

with open('salaries.txt') as f:
    salaries = []
    lines = f.readlines()
    for line in lines:
        name, salary = line.split(' - ')
        salaries.append(int(salary))
        if int(salary) > 20000:
            print(line, end='')
    print('\nСредняя зп: ', sum(salaries) / len(salaries))
