from collections import defaultdict

a = defaultdict()
print(a)  # defaultdict(None, {})

s = 'afgsdjfbabsvfgsahgdfjkadsfaghfsjdlbahjfgsdafjhbsdafvgsdfdasfbfdssadvfh'
c = defaultdict(int)
for char in s:
    c[char] += 1
print(c)  # defaultdict(<class 'int'>, {'a': 10, 'f': 12, 'g': 6, 's': 10, 'd': 9, 'j': 5, 'b': 5, 'v': 3,
# 'h': 5, 'k': 1, 'l': 1, ',': 1})

list_1 = [('cat', 1), ('dog', 5), ('cat', 3), ('dog', 2), ('cat', 6), ('dog', 4), ('cat', 8), ('dog', 9)]

d = defaultdict(list)
for animal, distance in list_1:
    d[animal].append(distance)  # defaultdict(<class 'list'>, {'cat': [1, 3, 6, 8], 'dog': [5, 2, 4, 9]})
print(d)
print('='*70)


e = defaultdict(lambda: "i don't know")
e['cat'] = 'Boris'
print(e['cat'])  # Boris
print(e['dog'])  # i don't know