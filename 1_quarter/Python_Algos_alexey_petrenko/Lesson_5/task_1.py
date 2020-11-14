from collections import Counter

a = Counter()
b = Counter('abrakadabra')
c = Counter({'cats': 10, 'dogs': 5})
print(a, b, c, sep='\n')

print(b['z'])
b['z'] = 3
#  **************************************************
print('*'*50)
print(b)  # Counter({'a': 5, 'z': 3, 'b': 2, 'r': 2, 'k': 1, 'd': 1})

print(b.most_common(3))  # [('a', 5), ('z', 3), ('b', 2)]
#  ==================================================
print("="*50)
d = Counter(a=4, b=-2, c=3)
e = Counter(a=2, b=3, c=4)
print(d, e, sep='\n')  # Counter({'a': 4, 'c': 3, 'b': -2}) and Counter({'c': 4, 'b': 3, 'a': 2})
print(d + e)  # Counter({'c': 7, 'a': 6, 'b': 1})
print(d - e)  # Counter({'a': 2})
print(d & e)  # Counter({'c': 3, 'a': 2})
print(d | e)  # Counter({'a': 4, 'c': 4, 'b': 3})
print(*d, *e)  # a b c a b c