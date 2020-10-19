# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь


# number = int(input('Enter your number, please: '))

# a, b, c = number // 100, number % 100 // 10, number % 10
# print('The sum is: ', a + b + c)
# print('The multiply is: ', a * b * c)

# ==============
#  Alternative Solution using cycles
num = input('Enter a 3 digit number: ')
num = str(num)

summa = 0
mult = 1

for i in num:
    summa += int(i)
    mult *= int(i)
print(f'The sum is {summa}')
print(f'The multiplication is {mult}')