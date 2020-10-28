BASE = 10


def sum_digits(number):
    if number < BASE:
        return number
    return number % BASE + sum_digits(number // BASE)


num = int(input('Enter natural number. The zero is exit'))
max_sum = 0
max_num = 0

while num != 0:
    spam_num = num
    spam_sum = sum_digits(num)
    if spam_num > max_sum:
        max_sum = spam_sum
        max_num = spam_num
    num = int(input('enter natural number. The zero is exit'))
print(f'The number {max_num} has maximum sum of digits: {max_sum}')