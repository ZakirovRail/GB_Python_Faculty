# file = open('123.txt')
# print(file)  # -> <_io.TextIOWrapper name='123.txt' mode='r' encoding='cp1252'>
# print(file.read())  # -> qwe rty uio
# file.close()
# -----------------------------------------------
# file = open('123.txt')
# lines = file.readlines()
# print(lines)  # -> ['qwe\n', 'rty\n', 'uio']
# file.close()
# -----------------------------------------------
# file = open('123.txt')
# line = file.readline()
# print(line, end='')  # -> qwe
# line = file.readline()
# print(line, end='\n')  # -> rty
# line = file.readline()
# print(line, end='')  # -> uio
# file.close()
# -----------------------------------------------
# file = open('123.txt')
# line = file.readline().strip() # remove all technical characters - \n
# print(line)
# line = file.readline()
# print(line)
# line = file.readline().strip()
# print(line)
# -----------------------------------------------

# f = open('234.txt', 'w')
# f.write('Something special should be here')
# f.close()

# f = open('234.txt', 'a')
# f.write('Adding a new lines to an existing file using the "a" argument for the "open" function \n')
# f.close()

# f = open('234.txt', 'a')
# f.writelines(['something', 'new', 'in', 'the', 'file'])  # getting an iterable object and add it to the file with concatination
# f.close()

# -----------------------------------------------

# with open('123.txt', 'w') as f:
#     f.writelines(['something\n', 'new\n', 'in\n', 'the\n', 'file\n'])
"""
something
new
in
the
file
"""

# -----------------------------------------------
"""
r - open for reading only
w - open for writing, but all existing cntent will be erased
x - open for writing, if this file does not exist. If file exists it won't be created
a - Open file for adding new data
b - open file in binary format
t - open file in text format (by default)
+ - open file for reading and writing 
"""
# -----------------------------------------------

# try:
#     f_obj = open("text.txt")
#     for line in f_obj:
#         print(line)
# except IOError:
#     print("Произошла ошибка вврда-вывода")
# finally:
#     f_obj.close()
# -----------------------------------------------
# Attributes of file: closed, mode, name
# with open('123.txt', 'r') as f:
#     print(f.mode)  # r
#     print(f.closed)  # False
#     print(f.name)  # 123.txt
# print(f.closed)  # True
# -----------------------------------------------
# Determin of pisition of cursor - tell(), seek()
# with open('123.txt', 'w+') as f_obj:
#     f_obj.write('qwe\nrty\nuio\nasd')
#     print(f_obj.read())
#     print(f_obj.tell())  # 18 позиция в байтах
#     print('============')
#     f_obj.seek(0) # переход на 0 позицию в файле, в самое начало
#     print(f_obj.read())
#
#     f_obj.seek(0)
#     print(len(f_obj.read()))  # 15
# -----------------------------------------------
# import os
# os.remove('123.txt')  #remove a file
# os.rename('123.txt', '12345.txt')
# os.mkdir('1.txt')
# os.rmdir()
# os.chmod()
# print(os.path.exists('123.txt'))  # True
# print(os.path.isdir('123.txt'))  # False
# -----------------------------------------------
# with open('123.txt', 'w', encoding= 'utf-8') as f:
#     print('Необычная работа функции print', file=f)
#------------------------------------------------
# import json
"""
serialisation
methods - dump() and dumps()
Python                        JSON
dict                            object
list, tuple                     array
str                             string
int, long, float                number
True                            true
False                           false
None                            null

deserialisation
methods - load() and loads() 
"""

# data = {'income': {'salary': 5000, 'bonus': 1000}}
#
# with open('data.json', 'w') as f:
#     json.dump(data, f)
#
# with open('data.json') as f:
#     data1 = json.load(f)
# print(data1)
# print(type(data1))

# -----------------------------------------------
# import shutil
# shutil.copy()
# shutil.copyfile() # copy without metadata
# shutil.rmtree('1.txt')  # analog of os.rmdir
