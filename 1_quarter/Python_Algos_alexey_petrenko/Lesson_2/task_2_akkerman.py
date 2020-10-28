import sys

sys.setrecursionlimit(10000) # change deep of recursion - DON"T CHANGE IT IF YOU ARE NOT SURE!!!


def akk(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    else:
        return akk(m - 1, akk(m, n - 1))


a = int(input('Enter the "m" value:'))
b = int(input('Enter the "n" value:'))

res = akk(a, b)
print(res)
