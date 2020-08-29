"""
6)	Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""



# Первое решение
def int_func(word):
    word_to_cap = str(word)
    return word_to_cap.capitalize()


print(int_func('string')) # -> String


# Второе решение


def int_func(list_word):
    list_to_cap = list_word.split(' ')
    new_list = []
    for word in list_to_cap:
        new_list.append(word.capitalize())
    return ' '.join(new_list)


print(int_func('string to be capitalized')) # -> String To Be Capitalized

#Solution from teacher
def int_func(text):
    return text.title()

print(int_func('text'))

res_int_func = int_func('text bla text')
print(res_int_func)