n = 1000
sieve = [i for i in range(n)]
sieve[1] = 0
for i in range(2, n):
    if sieve[i] != 0:
        j = i + i
        while j < n:
            sieve[j] = 0
            j += i
print(sieve)  # [0, 0, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0, 19, 0, 0, 0, 23, 0, 0, 0, 0, 0, 29....]

res = [i for i in sieve if i != 0 and i < 150]
print(res)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
# 103, 107, 109, 113, 127, 131, 137, 139, 149]
