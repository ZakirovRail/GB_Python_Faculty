import timeit
import cProfile


def fib_loop(n):
    if n < 2:
        return n
    first = 0
    second = 1

    for _ in range(2, n + 1):
        first, second = second, first + second
    return second


print(timeit.timeit('fib_loop(5)', number=100, globals=globals()))  #6.340199999999713e-05
print(timeit.timeit('fib_loop(10)', number=100, globals=globals()))  #6.340199999999713e-05
print(timeit.timeit('fib_loop(15)', number=100, globals=globals()))  #6.340199999999713e-05
print(timeit.timeit('fib_loop(20)', number=100, globals=globals()))  #6.340199999999713e-05
print(timeit.timeit('fib_loop(25)', number=100, globals=globals()))  #6.340199999999713e-05

cProfile.run('fib_loop(5)')  #
cProfile.run('fib_loop(10)')  #
cProfile.run('fib_loop(15)')  #
cProfile.run('fib_loop(20)')  #
cProfile.run('fib_loop(25)')  #


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

# test_fib(fib_loop)
