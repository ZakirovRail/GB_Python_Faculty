# class Car:
#     def __init__(self):
#         self.modules = []
#
#
# car = Car()
# module_1 = 'heating of a steering wheel'
# module_2 = 'heating of a front glass'
# car.modules.append(module_1)
# car.modules.append(module_2)
# print(car.modules) #  ['heating of a steering wheel', 'heating of a front glass']

# =====================================================================================
# class Car:
#     def __init__(self):
#         self.modules = []
#
#     def __add__(self, other):
#         self.modules.append(other)
#
# car = Car()
# module_1 = 'heating of a steering wheel'
# module_2 = 'heating of a front glass'
# car + module_1
# car + module_2
#
# print(car.modules)  #  ['heating of a steering wheel', 'heating of a front glass']
# =====================================================================================

# class Car:
#     def __init__(self):
#         self.modules = []
#
#     def __add__(self, other):
#         self.modules.append(other)
#
#     def __str__(self):   # описание как будет выглядеть принт для экземпляра класса
#         return f'Autos with modules: {self.modules}'
#
# car = Car()
# module_1 = 'heating of a steering wheel'
# module_2 = 'heating of a front glass'
# car + module_1
# car + module_2
#
# print(car)  # Autos with modules: ['heating of a steering wheel', 'heating of a front glass']

# =====================================================================================

# class Car:
#     def __init__(self):
#         self.modules = []
#
#     def __add__(self, other):
#         self.modules.append(other)
#
#     def __str__(self):   # описание как будет выглядеть принт для экземпляра класса
#         return f'Autos with modules: {self.modules}'
#
#     def __del__(self):
#         print('The object is deleted')
#
# car = Car()
# module_1 = 'heating of a steering wheel'
# module_2 = 'heating of a front glass'
# car + module_1
# car + module_2
#
# print(car)
"""
Autos with modules: ['heating of a steering wheel', 'heating of a front glass']
The object is deleted
"""

# =====================================================================================
# class Car:
#     def __init__(self):
#         self.modules = []
#
#     def __add__(self, other):
#         self.modules.append(other)
#
#     def __str__(self):   # описание как будет выглядеть принт для экземпляра класса
#         return f'Autos with modules: {self.modules}'
#
#     def __del__(self):
#         print('The object is deleted')
#
#     def __setattr__(self, key, value):  # для изменения логики создания аттрибутов
#         super().__setattr__(key, value)
#         print(f'Добавлен ключ {key} со значением {value}')
#
#
# car = Car()
# module_1 = 'heating of a steering wheel'
# module_2 = 'heating of a front glass'
# car + module_1
# car + module_2
# car.model = 'Tesla'
#
# print(car)
"""
Добавлен ключ modules со значением []
Добавлен ключ model со значением Tesla
Autos with modules: ['heating of a steering wheel', 'heating of a front glass']
The object is deleted
"""

# =====================================================================================
# class Car:
#     def __init__(self):
#         self.modules = []
#
#     def __add__(self, other):
#         self.modules.append(other)
#
#     def __str__(self):   # описание как будет выглядеть принт для экземпляра класса
#         return f'Autos with modules: {self.modules}'
#
#     def __del__(self):
#         print('The object is deleted')
#
#     def __setattr__(self, key, value):  # для изменения логики создания аттрибутов
#         # super().__setattr__(key, value)
#         self.__dict__[key] = value   # второй способ
#         print(f'Добавлен ключ {key} со значением {value}')
#
#
# car = Car()
# module_1 = 'heating of a steering wheel'
# module_2 = 'heating of a front glass'
# car + module_1
# car + module_2
# car.model = 'Tesla'

# print(car)
"""
Добавлен ключ modules со значением []
Добавлен ключ model со значением Tesla
Autos with modules: ['heating of a steering wheel', 'heating of a front glass']
The object is deleted
"""

# =====================================================================================
# class Car:
#     def __init__(self):
#         self.modules = []
#
#     def __add__(self, other):
#         self.modules.append(other)
#
#     def __str__(self):   # описание как будет выглядеть принт для экземпляра класса
#         return f'Autos with modules: {self.modules}'
#
#     def __del__(self):
#         print('The object is deleted')
#
#     def __setattr__(self, key, value):  # для изменения логики создания аттрибутов
#         super().__setattr__(key, value)
#         print(f'Добавлен ключ {key} со значением {value}')
#
#     def __getitem__(self, item):
#         return self.modules[item]
#
# car = Car()
# module_1 = 'heating of a steering wheel'
# module_2 = 'heating of a front glass'
# car + module_1
# car + module_2
# car.model = 'Tesla'
#
# # print(car)
# print(car[1])  # heating of a front glass
"""
Добавлен ключ modules со значением []
Добавлен ключ model со значением Tesla
heating of a front glass
The object is deleted
"""

# =====================================================================================
# class Car:
#     def __init__(self):
#         self.modules = []
#
#     def __add__(self, other):
#         self.modules.append(other)
#
#     def __str__(self):   # описание как будет выглядеть принт для экземпляра класса
#         return f'Autos with modules: {self.modules}'
#
#     def __del__(self):
#         print('The object is deleted')
#
#     def __setattr__(self, key, value):  # для изменения логики создания аттрибутов
#         super().__setattr__(key, value)
#         print(f'Добавлен ключ {key} со значением {value}')
#
#     def __getitem__(self, item):
#         return self.modules[item]
#
#     def __call__(self, price = None):
#         print(f'The car {self.model} with moduels {self.modules}, with the price {price}')
#
# car = Car()
# module_1 = 'heating of a steering wheel'
# module_2 = 'heating of a front glass'
# car + module_1
# car + module_2
# car.model = 'Tesla'
#
# car(5000)  #The car Tesla with moduels ['heating of a steering wheel', 'heating of a front glass'], with the price 5000

"""
Добавлен ключ modules со значением []
Добавлен ключ model со значением Tesla
The car Tesla with moduels ['heating of a steering wheel', 'heating of a front glass'], with the price 5000
The object is deleted
"""

# =====================================================================================
# class Car:
#     def __init__(self):
#         self.modules = []
#         self.fc = 7
#
#     def __add__(self, other):
#         self.modules.append(other)
#
#     def __str__(self):   # описание как будет выглядеть принт для экземпляра класса
#         return f'Autos with modules: {self.modules}'
#
#     # def __del__(self):
#     #     print('The object is deleted')
#
#     # def __setattr__(self, key, value):  # для изменения логики создания аттрибутов
#     #     super().__setattr__(key, value)
#     #     print(f'Добавлен ключ {key} со значением {value}')
#
#     def __getitem__(self, item):
#         return self.modules[item]
#
#     def __call__(self, price = None):
#         print(f'The car {self.model} with moduels {self.modules}, with the price {price}')
#
#     def __eq__(self, other):
#         return self.fc == other
#
# car = Car()
# module_1 = 'heating of a steering wheel'
# module_2 = 'heating of a front glass'
# car + module_1
# car + module_2
# car.model = 'Tesla'
#
# car(5000)  #The car Tesla with moduels ['heating of a steering wheel', 'heating of a front glass'], with the price 5000
# print(car == 7)  # True
# print(car == 50)  # False


"""
The car Tesla with moduels ['heating of a steering wheel', 'heating of a front glass'], with the price 5000
True
False
"""


# =====================================================================================

# from abc import ABC, abstractmethod
#
#
# class MyAbcMethod(ABC):
#     @abstractmethod
#     def my_method_1(self):
#         pass
#
#     @abstractmethod
#     def my_method_2(self):
#         pass
#
#
# class MyClass(MyAbcMethod):
#     def my_method_1(self):
#         pass
#
#     def my_method_2(self):
#         pass
#
#
# mc = MyClass()
# =====================================================================================

# for i in [1,2,3,4,5,6]:  # __iter__ => __next__ => raise StopIteration
#     print(i)

# class Iterator:
#     def __init__(self):
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i < 5:
#             return self.i
#         else:
#             raise StopIteration
#
# qwe = Iterator()
# for i in qwe:
#     print(i)

# =====================================================================================


# class Human:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
# #code
#
# human = Human('Ivan', 'Ivanov', 30)
# print(human.age)
# print(human.name)
# print(human.surname)


# class Human:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self._age = age
#
#     @property
#     def age(self):
#         #if self.age ...
#         return self.
#
# #code
#
# human = Human('Ivan', 'Ivanov', 30)
# print(human.age)

# =====================================================================================

class WinDoor:
    def __init__(self, wd_len, wd_hei):
        self.square = wd_len * wd_hei


class Room:
    def __init__(self, len1, len2, h):
        self.square = 2 * h * (len1 + len2)
        self.wd = []

    def add_windoor(self, wd_len, wd_hei):
        self.wd.append(WinDoor(wd_len, wd_hei))

    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square
        return main_square


r = Room(7, 12, 3.7)
print(r.square)
r.add_windoor(2, 3)
r.add_windoor(2, 3)
print(r.common_square())



