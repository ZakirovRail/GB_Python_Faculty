# version 1
from collections import Counter

origin_string = 'beep boop beer!'

letters_counter = Counter(origin_string)
print(letters_counter)  # ['b', 'e', 'e', 'p', ' ', 'b', 'o', 'o', 'p', ' ', 'b', 'e', 'e', 'r', '!']
print(dict(letters_counter))  # {'b': 3, 'e': 4, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1}

# =====================================================================================================================
# version 2
origin_string = 'beep boop beer!'
list_string = [i for i in origin_string]
# print(list_string)  # ['b', 'e', 'e', 'p', ' ', 'b', 'o', 'o', 'p', ' ', 'b', 'e', 'e', 'r', '!']
new_dict = {}

for i in list_string:
    if i in new_dict:
        new_dict[i] += 1
    else:
        new_dict[i] = 1
print(new_dict)  # {'b': 3, 'e': 4, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1}
