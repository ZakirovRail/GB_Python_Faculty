print('Enter three digits: ')
a = int(input('1st - '))
b = int(input('2nd - '))
c = int(input('3rd - '))

if b < a < c or c < a < b:
    print('Medium: ', a)
elif a < b < c or c < b < a:
    print('Medium: ', b)
else:
    print('Medium: ', c)
