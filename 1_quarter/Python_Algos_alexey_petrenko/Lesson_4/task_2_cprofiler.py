import cProfile


def my_len(a):
    return len(a)


def my_sum(a):
    s = 0
    for item in a:
        s += item
        return s


def main():
    array = [i for i in range(100)]
    len_ = my_len(array)
    sum_ = my_sum(array)


cProfile.run('main()')
