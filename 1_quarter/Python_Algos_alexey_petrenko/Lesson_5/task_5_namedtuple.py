from collections import namedtuple

hero_1 = ('Aaz', 'Izverg', 250, 0.0, 100)

print(hero_1[1])


class Person:
    def __init__(self, name, race, health, mana, armor):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.armor = armor

    def __str__(self):
        return f'name = {self.name}'


hero_2 = Person('Aaz', 'Izverg', 250, 0.0, 100)

print(hero_2.mana)  # 0.0
print(hero_2)  # name = Aaz

print('===============================================================================================================')
PersonNew = namedtuple('PersonNew', 'name, race, health, mana, armor')

hero_3 = PersonNew('Aaz', 'Izverg', 250, 0.0, 100)
print(hero_3.race)  # Izverg
print(hero_3)  # PersonNew(name='Aaz', race='Izverg', health=250, mana=0.0, armor=100)

# hero_3.mana = 100 #  will envoke an error
hero_3 = hero_3._replace(mana=100)
print(hero_3.mana)  # 100
print(hero_3._fields)  # ('name', 'race', 'health', 'mana', 'armor')
