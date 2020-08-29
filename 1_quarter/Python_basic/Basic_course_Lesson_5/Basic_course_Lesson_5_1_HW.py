"""
1)	Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

# ex = False
# data_from_user = []
# # принимаем вводимые пользователем данные, пока он не оставит пустую строку и сохраняем в список data_from_user
# while ex is False:
#     from_user = input('Enter your data or leave an empty row and push the "Enter" key to exit: ').split('\n')
#     for line in from_user:
#         if not line:
#             ex = True
#             break
#         data_from_user.append(line)
# print(data_from_user)
#
# # проходим по списку и построчно добавляем с использовнеи переноса строки
# with open('user_data.txt', 'w', encoding='utf-8') as f:
#     for line in data_from_user:
#         # f.writelines(line, '\n')
#         f.write(line)
#         f.write('\n')

# Solution from teacher
with open('test.txt', 'w') as f:
    while True:
        line = input('Введите строку: ')
        if line == '':
            break
        f.write(line + '\n')
