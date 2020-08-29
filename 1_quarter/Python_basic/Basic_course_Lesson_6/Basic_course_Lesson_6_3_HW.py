"""
3)	Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с
учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры
класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

positions = {'Manager': {'wage': 1000, 'bonus': 100}, 'Team Leader': {'wage': 700, 'bonus': 80},
             'Senior Engineer': {'wage': 500, 'bonus': 60}, 'Regular Engineer': {'wage': 350, 'bonus': 35}}


# print(positions['Manager']['wage'] + positions['Manager']['bonus'])

# class Worker:
#     def __init__(self, name, surname, position):
#         self.name = name
#         self.surname = surname
#         self._position = position
#
#
# class Position(Worker):
#     def get_full_name(self, name, surname, position):
#         print('The full name is {} {}'.format(name, surname))
#
#     def get_total_income(self, position):
#         print(positions[position]['wage'] + positions[position]['bonus'])
#
#
# manager = Position(name='John', surname='Connor', position='Manager')
# print(manager.name)
# print(manager.surname)
# print(manager._position)
#
# manager.get_full_name(name='John', surname='Connor', position='Manager')
# manager.get_total_income('Manager')


# Solution from teacher

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname, self.position)

    def get_total_income(self):
        print(self._income_wage + self._income_bonus)


pos = Position('Ivan', 'Ivanov', 'senior', {'wage': 150000, 'bonus': 50000})
pos.get_full_name()
pos.get_total_income()
