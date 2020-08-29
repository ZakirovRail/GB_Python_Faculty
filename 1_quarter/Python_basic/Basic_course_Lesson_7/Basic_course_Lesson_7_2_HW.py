"""
2)	Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod

# class Clothes:
#     def __init__(self, size, height):
#         # self.coat = coat
#         # self.suit = suit
#         self.size = size
#         self.height = height
#
#     @abstractmethod
#     def calc_coat(self):
#         return (self.size / 6.5 + 0.5)
#
#     @abstractmethod
#     def calc_suit(self):
#         return (self.height * 2 + 0.3)
#
#
# suit_1 = Clothes(45, 179)
# coat_1 = Clothes(45, 179)
# print(suit_1.calc_suit())
# print(suit_1.calc_coat())


# ------------------------------------------------------------


# class Clothes:
#     def __init__(self, size, height):
#         # self.coat = coat
#         # self.suit = suit
#         self.size = size
#         self.height = height
#
#     @property
#     def calc_coat(self):
#         return (self.size / 6.5 + 0.5)
#
#     @property
#     def calc_suit(self):
#         return (self.height * 2 + 0.3)
#
#
# suit_2 = Clothes(40, 170)
# coat_2 = Clothes(40, 170)
#
# print(suit_2.calc_suit)  # @property
# print(suit_2.calc_coat)  # @property


# Solution from teacher

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return round((self.param / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calculate(self):
        return round((2 ** self.param) + 0.3)


coat = Coat(45)
suit = Suit(170)
print(coat.calculate)
print(suit.calculate)
