"""
4)	Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
name, is_police (булево).  А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar,
SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
"""


# class Car:
#     def __init__(self, speed, color, name, is_police=False):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print('Car goes somewhere')
#
#     def stop(self):
#         print('car is stopped')
#
#     def turn(self, direction):
#         self.direction = direction
#         print(f'car is turned to the {direction} direction')
#
#     def show_speed(self, speed):
#         self.speed = speed
#         return speed
#         # print(f'The current speed is {current_speed}')
#
#
# class TownCar(Car):
#     is_police = False
#     speed = 80
#     color = 'green'
#     name = 'Toyota'
#     if speed > 60:
#         print(f'The current speed is {speed} it is more than 60')
#
#     def show_speed(self, current_speed):
#         print(f'New method inside class TownCar which is shown a speed of a car, which is {current_speed}')
#
#
# class SportCar(Car):
#     is_police = False
#     speed = 45
#     color = 'red'
#     name = 'BMV'
#     if speed > 60:
#         print(f'The current speed is {speed} it is more than 60')
#
#
# class WorkCar(Car):
#     is_police = False
#     speed_work = 35
#     color = 'black'
#     name = 'Niva'
#     if speed_work > 60:
#         print(f'The current speed is {speed_work} it is more than 60')
#
#     def show_speed(self, current_speed):
#         print(f'New method inside class WorkCar, will shown a speed of a car, which is {current_speed}')
#
#
# class PoliceCar(Car):
#     is_police = True
#     speed = 50
#     color = 'white'
#     name = 'Shevrolet'
#     if speed > 60:
#         print(f'The current speed is {speed} it is more than 60')
#
#
# town = TownCar(speed=75, color='white', name='Audi', is_police=False)
# print(town.speed)
# print(town.is_police)
# print(town.name)
# print(town.color)
# town.show_speed(80)
#
# sport = SportCar
# print(sport.speed)
# print(sport.is_police)
# print(sport.name)
# print(sport.color)
#
# work = WorkCar(speed=75, color='white', name='Audi', is_police=False)
# print(work.speed)
# print(work.is_police)
# print(work.name)
# print(work.color)
# work.show_speed(current_speed=95)
#
# police = PoliceCar
# print(police.speed)
# print(police.is_police)
# print(police.name)
# print(police.color)


# Solution from teacher


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = is_police

    def go(self):
        print('{} is going'.format(self.name))

    def stop(self):
        print('{} is stopping'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}'.format(self.name, direction))

    def show_speed(self):
        print('Current speed: ', self.speed)


class TownCar(Car):
    def show_speed(self):
        print('Current speed: ', self.speed)
        if self.speed > 60:
            print('Warning! Your speed is more than max!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Current speed: ', self.speed)
        if self.speed > 40:
            print('Warning! Your speed is more than max!')


class PoliceCar(Car):
    pass


sport_car = SportCar(240, 'Red', 'Sport Car', False)
town_car = TownCar(140, 'Grey', 'Town Car', False)
work_car = WorkCar(90, 'Yellow', 'Work Car', False)
police_car = PoliceCar(210, 'Blue', 'Police Car', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
