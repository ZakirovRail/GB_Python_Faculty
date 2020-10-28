def func(a, b):
    """

    :param a:
    :param b:
    :return:

    func(1, 4)
    '1,2,3,4'
    """

    if a == b:
        return f'{a}'
    if a < b:
        return f'{a}, {func(a + 1, b)}'
    if a > b:
        return f'{a}, {func(a - 1, b)}'


print(func(1, 10))
print(func(10, 4))