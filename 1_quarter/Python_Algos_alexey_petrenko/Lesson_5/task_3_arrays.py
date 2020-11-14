from collections import deque

a = deque()
b = deque('abracadabra')
c = deque([1, 2, 3, 4, 5])

print(a, b, c, sep='\n')
"""
deque([])
deque(['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a'])
deque([1, 2, 3, 4, 5])
"""

print('=' * 50)

d = deque([1, 2, 3])
print(d)  # deque([1, 2, 3])
d.append(4)
print(d)  # deque([1, 2, 3, 4])

d.appendleft(5)
print(d)  # deque([5, 1, 2, 3, 4])

d.extend([6, 7])
print(d)  # deque([5, 1, 2, 3, 4, 6, 7])
print('=' * 50)

d.extendleft([8, 9])
print(d)  # deque([9, 8, 5, 1, 2, 3, 4, 6, 7])
print('=' * 50)

spam = d.pop()
print(d, spam)  # deque([9, 8, 5, 1, 2, 3, 4, 6]) 7

eggs = d.popleft()
print(d, eggs)  # deque([8, 5, 1, 2, 3, 4, 6]) 9

d.reverse()
print(d)  # deque([6, 4, 3, 2, 1, 5, 8])

d.rotate(2)
print(d)  # deque([5, 8, 6, 4, 3, 2, 1])
