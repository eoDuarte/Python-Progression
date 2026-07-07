import random
from abc import ABC, abstractmethod
from rich import print


class Character(ABC):
    def __init__(self, name, life=0):
        self.name = name
        self.life = life
        self.strikes = []

    def Attack(self, target, attack_level=100):
        if self.life > 0 and target.life > 0:
            strike = self.strikes[random.randrange(0, len(self.strikes))]
            print(f"{self.name} ({self.life}) attack {target.name}({target.life}) with a {strike} of {attack_level} force damage")
            target.Demage(attack_level)
        else:
            print(f"the Attack {self.name} -> {target.name} can't happen")
    def Demage(self, demage=0):
        factor = random.randint(0, demage)
        self.life = self.life - factor
        if self.life < 0:
            self.life = 0
        print(f"[blue]{self.name}[/] took [red]{factor} demage[/]")

    @abstractmethod
    def Heal(self):
        pass


class Warrior(Character):
    def __init__(self, name, life):
        super().__init__(name, life)
        self.strikes = ["punch", "axe blow", "spinning jump"]
    def Heal(self):
        factor = random.randint(0,100)
        self.life += factor
        print(f"{self.name}missed a bandage and recovered {factor} health points")


class Wizard(Character):
    def __init__(self, name, life):
        super().__init__(name, life)
        self.strikes = ["fireball", "ray of light", "static magic"]
    def Heal(self):
        factor = random.randint(0, 100)
        self.life += factor
        print(f"{self.name}performed a healing spell and recovered {factor} health points")
