BASE = 10

num = int(input('Enter number of digits: '))
digit = int(input('Which digit to calculate:'))
count = 0

for i in range(1, num + 1):
    ans = int(input(f'enter a number {i}: '))
    while ans > 0:
        if ans % BASE == digit:
            count += 1
        ans //= BASE

print(f'Were entered {count} digits {digit}')
