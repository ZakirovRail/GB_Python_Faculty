"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

# a = int(input('Enter a result for the 1st day: '))
# b = int(input('Enter a goal: '))
#
# result = a
# day = 1
#
# while result < b:
#     day += 1
#     result += result*0.1
# print(f'The result is no less then {b} km at the {day} day')

# solution from teacher
while True:
    days = 1
    start_km = int(input('Start result: '))
    last_km = int(input('Final resutl: '))

    if start_km > last_km:
        print('The entered data is wrong')
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1
        print('Sportsman will achieve results during {} days'.format(days))
        break
