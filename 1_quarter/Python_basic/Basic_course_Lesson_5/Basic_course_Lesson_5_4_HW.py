"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл.
"""
# equivalent_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять', 'Six': 'Шесть',
#                    'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять'}
# new_data = []
#
# with open('file_4_1.txt', 'r', encoding='utf-8') as or_file:
#     lines = or_file.readlines()
#
# for line in lines:
#     row = line.split()
#     row[0] = equivalent_dict[row[0]]
#     new_data.append(' '.join(row))
# print(new_data)
#
# with open('file_4_2.txt', 'a', encoding='utf-8') as fin_file:
#     for line in new_data:
#         fin_file.write(line)
#         fin_file.write('\n')

# Вопрос - как заменить ключи в словаре?

# Solution from teacher

with open('eng.txt') as f:
    lines = f.readlines()

with open('rus.txt', 'w') as f:
    for line in lines:
        if '1' in line:
            line = line.replace('One', 'Один')
        elif '2' in line:
            line = line.replace('Two', 'Два')
        elif '3' in line:
            line = line.replace('Three', 'Три')
        elif '4' in line:
            line = line.replace('Four', 'Четыре')
        f.write(line)
