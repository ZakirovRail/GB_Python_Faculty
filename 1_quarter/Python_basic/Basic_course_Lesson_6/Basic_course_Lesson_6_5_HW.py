"""
5)	Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут
title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         print('Запуск отрисовки')
#
#
# class Pen(Stationery):
#     def draw(self):
#         print('Переопределение метода draw для класса Pen')
#
#
# class Pencil(Stationery):
#     def draw(self):
#         print('Переопределение метода draw для класса Pencil')
#
#
# class Handle(Stationery):
#     def draw(self):
#         print('Переопределение метода draw для класса Handle')


# Solution from teacher


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Run of draw')


class Pen(Stationery):
    def draw(self):
        print('The pen draws')


class Pencil(Stationery):
    def draw(self):
        print('The pencil draws')


class Handle(Stationery):
    def draw(self):
        print('The pencil draws')


pen = Pen('pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')

pen.draw()
pencil.draw()
handle.draw()
