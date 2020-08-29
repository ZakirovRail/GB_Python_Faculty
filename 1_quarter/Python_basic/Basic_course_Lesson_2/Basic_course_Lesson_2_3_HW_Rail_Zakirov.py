"""
3)	Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""
# решение через dict
seasons = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Autumn',
    12: 'Winter',
}

month = int(input('Enter a number month: '))

if 1 <= month <= 12:
    print(f'The season is {seasons.get(month)}')
else:
    print('wrong number of month')



# решение через list

if month in (1, 2, 12):
    print('It is the winter season')
elif month in (3,4,5):
    print('It is the Spring season')
elif month in (6,7,8):
    print('It is the Summer season')
elif month in (9,10,11):
    print('It is the Autumn season')
else:
    print('You entered a wrong number of month')
