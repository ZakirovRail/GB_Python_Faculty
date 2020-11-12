import timeit
import cProfile

# a = [i for i in range(1000)]

# Очень важно, для корректных замеров, надо менять объем данных, а не количество замеров!!!
# print(timeit.timeit('a = [i for i in range(100)]', number=100))  # 0.0003347570000000015
# print(timeit.timeit('a = [i for i in range(1000)]', number=100))  # 0.003853281999999996
# print(timeit.timeit('a = [i for i in range(10000)]', number=100))  # 0.046906416
# print(timeit.timeit('a = [i for i in range(100000)]', number=100))  # 0.323956046
# print(timeit.timeit('a = [i for i in range(1000000)]', number=100))  # 5.496866855
print('*' * 50)


# Example 2


# def func(N):
#     for i in range(N):
#         for j in range(N):
#             for k in range(N):
#                 a = 0


# globals = это обязательный параметр, для анализа внешних функций
# print(timeit.timeit('func(2)', number=100, globals=globals()))  # 0.00022426199999999938
# print(timeit.timeit('func(4)', number=100, globals=globals()))  # 0.0007276550000000007
# print(timeit.timeit('func(6)', number=100, globals=globals()))  # 0.0015954780000000009
# print(timeit.timeit('func(8)', number=100, globals=globals()))  # 0.0030559570000000015
# print(timeit.timeit('func(10)', number=100, globals=globals()))  # 0.005304707999999998


# Example 2











