"""
4)	Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_words = input('Enter your words separated by backspace: ')

list_of_words = user_words.split(' ')
for word in list_of_words:
    print(word[0:11])
