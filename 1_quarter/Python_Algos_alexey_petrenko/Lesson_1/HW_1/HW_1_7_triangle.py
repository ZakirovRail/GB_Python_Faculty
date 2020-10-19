a = float(input('Enter a side of a triangle: '))
b = float(input('Enter a side of a triangle: '))
c = float(input('Enter a side of a triangle: '))

if a + b <= c or a + c <= b or b + c <= a:
    print('The triangle does not exist')
elif a != b and a != c and b != c:
    print('The triangle is different side')
elif a == b == c:
    print('The triangle is equal side')
else:
    print('The triangle has 2 equal sides')
