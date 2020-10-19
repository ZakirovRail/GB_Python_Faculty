# По введенным пользователем координатам двух точек вывести уравнение
# прямой вида y = kx + b, проходящей через эти точки.

print('Enter coordinates for a point A(x1, y1):')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

print('Enter coordinates for a point B(x2, y2), where B != A:')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

print('The equation of direct going through these two points is: ')
if x1 == x2:
    print(f'x = {x:.3f}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'y = {k:.3f} * x + {b:.3f}')