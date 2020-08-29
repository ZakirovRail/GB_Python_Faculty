"""
2)	Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


# class Road:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#         self.weight = 25 # постоянный коэфициент,  которй бущет постоянно глобальной переменной
#
#     def calculation(self, depth):
#         mass = depth * self.__length * self.__width * self.weight
#         return mass
#
#
# # В классе указываем длинну и ширину дороги
# Moscow_to_SaintPetersburg = Road(length=6000, width=15)
# # вызывая метод уточняем какой толщины будет дорожное полотно
# print(Moscow_to_SaintPetersburg.calculation(30))  # -> 67500000


# Solution from teacher
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        mass = self._length * self._width * 25 * 5 / 10
        print(mass, 'т')


my_road = Road(20, 5000)
my_road.calc_mass()
