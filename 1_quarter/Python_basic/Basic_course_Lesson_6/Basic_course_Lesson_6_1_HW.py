"""
1)	Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном
порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""
# import time
#
#
# class TrafficLight:
#     def __init__(self, color):
#         self._color = color
#
#     def running(self):
#         finished_color = None
#         if self._color == 'red':
#             print('red color 7 seconds')
#             time.sleep(7)
#             print('yellow color 2 seconds')
#             time.sleep(2)
#             print('green color 5 seconds')
#             time.sleep(5)
#         # return finished_color == 'red'
#         elif self._color == 'yellow':
#             print('yellow color 2 seconds')
#             time.sleep(2)
#             print('green color 5 seconds')
#             time.sleep(5)
#         # return finished_color == 'yellow'
#         elif self._color == 'yellow':
#             print('green color 5 seconds')
#             time.sleep(5)
#         # return finished_color == 'green'
#
#
# red = TrafficLight('red')
# red.running()
#
#
# yellow = TrafficLight('yellow')
# yellow.running()


# Solution from the teacher

from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = (('Red', 5), ('Yellow', 2), ('Green', 4))

    def running(self):
        for color, sec in cycle(self.__color):
            print(color, '(wait {} sec)'.format(sec))
            sleep(sec)


traffic = TrafficLight()

traffic.running()
