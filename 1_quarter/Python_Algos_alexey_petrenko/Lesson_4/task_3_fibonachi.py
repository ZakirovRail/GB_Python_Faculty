import timeit
import cProfile


# Example 1 - Recursion

# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)


# print(timeit.timeit('fib(5)', number=100, globals=globals()))  # 0.00022698799999999741
# print(timeit.timeit('fib(10)', number=100, globals=globals()))  # 0.0024061119999999984
# print(timeit.timeit('fib(15)', number=100, globals=globals()))  # 0.027911861000000003
# print(timeit.timeit('fib(20)', number=100, globals=globals()))  # 0.227237992
# print(timeit.timeit('fib(25)', number=100, globals=globals()))  # 2.3880928920000004

# cProfile.run('fib(5)')  # 15/1    0.000    0.000    0.000    0.000 task_3_fibonachi.py:7(fib)
# cProfile.run('fib(10)')  # 177/1    0.000    0.000    0.000    0.000 task_3_fibonachi.py:7(fib)
# cProfile.run('fib(15)')  # 1973/1    0.001    0.000    0.001    0.001 task_3_fibonachi.py:7(fib)
# cProfile.run('fib(20)')  # 21891/1    0.007    0.000    0.007    0.007 task_3_fibonachi.py:7(fib)
# cProfile.run('fib(25)')  # 242785/1    0.075    0.000    0.075    0.075 task_3_fibonachi.py:7(fib)


# def test_fib(func):
#     lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#     for i, item in enumerate(lst):
#         assert item == func(i)
#         print(f'Test {i} OK')

# test_fib(fib)

# =======================================================================================================================
# Example 2 - Recursion + dictionary(технология мемоизации - хранения промежуточных результатов) для ускорения


def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n - 2)
        return fib_d[n]

    return _fib_dict(n)


print(timeit.timeit('fib_dict(5)', number=100, globals=globals()))  # 0.0002437669999999989
print(timeit.timeit('fib_dict(10)', number=100, globals=globals()))  # 0.0004475320000000005
print(timeit.timeit('fib_dict(15)', number=100, globals=globals()))  # 0.0006369159999999978
print(timeit.timeit('fib_dict(20)', number=100, globals=globals()))  # 0.0007989719999999985
print(timeit.timeit('fib_dict(25)', number=100, globals=globals()))  # 0.001137746999999998


cProfile.run('fib_dict(5)')  # 9/1    0.000    0.000    0.000    0.000 task_3_fibonachi.py:42(_fib_dict)
cProfile.run('fib_dict(10)')  # 19/1    0.000    0.000    0.000    0.000 task_3_fibonachi.py:42(_fib_dict)
cProfile.run('fib_dict(15)')  # 29/1    0.000    0.000    0.000    0.000 task_3_fibonachi.py:42(_fib_dict)
cProfile.run('fib_dict(20)')  # 39/1    0.000    0.000    0.000    0.000 task_3_fibonachi.py:42(_fib_dict)
cProfile.run('fib_dict(25)')  # 49/1    0.000    0.000    0.000    0.000 task_3_fibonachi.py:42(_fib_dict)


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


# test_fib(fib_dict)
