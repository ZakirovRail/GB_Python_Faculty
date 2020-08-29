"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

# with open('file_2.txt', 'r', encoding='utf-8') as f_file:
#     counter_lines = 0
#     number_words = 0
#     for line in f_file:
#         counter_lines += 1
#         number_words = len(line.split(' '))
#         print('Line number {} and the number of words in the line is {}'.format(counter_lines, number_words))
# print('The total number of lines is {}'.format(counter_lines))

# Solution from teacher
with open('test.txt') as f:
    lines = f.readlines()
    print('Количество строк: ', len(lines))
    for num_line, line in enumerate(lines, start=1):
        print('{} строка содержит - {} слов'.format(num_line, len(line.split())))
