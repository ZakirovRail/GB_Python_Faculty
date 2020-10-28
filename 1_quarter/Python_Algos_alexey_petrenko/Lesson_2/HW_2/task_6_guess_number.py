import random

num = random.randint(0, 100)
print('Try to guess a number from 0 to 100 during 10 attempts: ')

for i in range(1, 11):
    answer = int(input(f'Attempt {i}: '))
    if num < answer:
        print('The number is less')
    elif num > answer:
        print('The number is greater')
    else:
        print(f"You win with {i} attempt")
        break
else:
    print(f'Fail. The number was {num}')
print('After')
