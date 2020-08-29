# class DataBaseConnection:
#     def connect(self):
#         print('connecting')
#
#     @staticmethod
#     def select(a = 5):
#         print('selecting', a)
#
# data = DataBaseConnection()
# data.connect()
# data.select(a=10)
#
# DataBaseConnection.select(a=20)

# ------------------------------------------------

# class DataBaseConnection:
#     def connect(self):
#         print('connecting')
#
#     @staticmethod
#     def select(a = 5):
#         print('selecting', a)
#
#     @classmethod
#     def my_method(cls, param):
#         print(cls, param)
#
# DataBaseConnection.my_method(44)

# ------------------------------------------------

# class Customer:
#     """
#     Description of this class
#     """
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# john = Customer('John', 50)
# print(john)
# print(john.age)  # 50
# print(john.name)  # John
# print(john.__dict__)  # {'name': 'John', 'age': 50}
# print(john.__doc__)  #     Description of this class
# print(john.__class__)  # <class '__main__.Customer'
# print(john.__class__.__name__)  # Customer
# print(john.__module__)  # __main__

# ============================================================================

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return f'{self.name} {self.surname}'
#
#
# class Teacher(Person):
#
#     def to_teach(self, subj, *pupils):
#         for pupil in pupils:
#             pupil.to_take(subj)
#
#
# class Pupil(Person):
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
#         self.knowledges = []
#
#     def to_take(self, subj):
#         self.knowledges.append(subj)
#
#
# class Subject:
#     def __init__(self, *subjects):
#         self.subjects = subjects
#
#     def my_list(self):
#         return self.subjects
#
#
# s = Subject('math', 'physics')
# t = Teacher('Ivan', 'Ivanov')
# print(t)
# p_1 = Pupil('Pert', 'Petrov')
# p_2 = Pupil('Sidr', 'Sidorov')
# p_3 = Pupil('Kirill', 'Kirillov')
# print(p_1, p_2, p_3)
#
#
# t.to_teach(s, p_1, p_2)
# print(p_1.knowledges[0].my_list())
# print(p_2.knowledges[0].my_list())
# ============================================================================

#Exceptions

# class OwnError(Exception):
#     def __init__(self, t):
#         self.txt = t
#
# input_data = input('введите положительное число')
#
# try:
#     input_data = int(input_data)
#     if input_data < 0:
#         raise OwnError('Вы ввели не число!')
# except ValueError:
#     print('Вы ввели не число')
# except OwnError as err:
#     print(err)
# ============================================================================

# import psutil
# print(psutil.disk_usage('C:'))
# print(psutil.virtual_memory())
# ============================================================================
import requests

response = requests.get('https://www.bbc.com')
print(response.content)


















































