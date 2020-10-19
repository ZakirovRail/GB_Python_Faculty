num = int(input('The number of letter in alphabet (1-26): '))
num = ord('a') + num - 1

print(f'It is the letter {chr(num)}')

FIRST_LETTER = 96
num = int(input('The number of letter in alphabet (1-26): '))
num = FIRST_LETTER + num
print(f'It is the letter {chr(num)}')
