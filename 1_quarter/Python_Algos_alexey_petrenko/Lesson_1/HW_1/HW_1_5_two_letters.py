import string

first = ord(input('1st letter: '))
second = ord(input('2nd letter: '))
first = first - ord('a') + 1
second = second - ord('a') + 1

print(f'1st letter in the row is = {first}, 2nd = {second}')
print(f'Number letters between these two letters = {abs(first - second - 1)}')

a = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
b = string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
c = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
d = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
e = string.digits  # 0123456789

print(a)
print(b)
print(c)
print(d)
print(e)