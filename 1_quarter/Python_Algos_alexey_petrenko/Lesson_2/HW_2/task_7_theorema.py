def sum_natural(n):
    assert n < 999, 'To high number'
    if n == 1:
        return n
    sum_n = n + sum_natural(n - 1)
    return sum_n


n = int(input('Enter any natural number:'))
left = sum_natural(n)
right = n * (n + 1) // 2

print(f'left = {left}')
print(f'right = {right}')
print('Right' if left == right else 'Wrong')
