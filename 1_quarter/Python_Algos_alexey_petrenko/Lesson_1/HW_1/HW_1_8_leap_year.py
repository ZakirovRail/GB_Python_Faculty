year = int(input('Enter a year: '))

if year % 4 or year // 100 == 0 and year % 400 != 0:
    print('Usual')
else:
    print('Leap')

#  Alternative way
# if year % 4 != 0:
#     print('Usual')
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print('Leap')
#     else:
#         print('Usual')
# else:
#     print('Leap')
