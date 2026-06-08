from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name="", life=0, attack=0):
        self.name = name
        self.life = life
        self.attack = attack

    def Attack(self, target="", strength=0):
        pass

    def Demage(self, demage=0):
        pass

    @abstractmethod
    def Heal(self):
        pass


class Warrior(Character):
    def Heal(self):
        pass

class Wizard(Character):
    def Heal(self):
        pass