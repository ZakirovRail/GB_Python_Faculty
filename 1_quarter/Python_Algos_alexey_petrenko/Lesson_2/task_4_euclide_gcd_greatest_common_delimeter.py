def gcd_1(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


# print(gcd_1(42, 12))  # 6


def gcd_2(a, b):
    if b == 0:
        return a
    return gcd_2(b, a % b)


# print(gcd_1(426454562, 12))
# print(gcd_2(426454562, 12))


def gcd_3(a, b):
    while b != 0:
        a, b = b, a % b
        # temp = b
        # b = a % b
        # a = temp
    return a


print(gcd_1(426454562, 12))
print(gcd_2(426454562, 12))
print(gcd_3(426454562, 12))
