from character import *
from rich import inspect


def main():
    p1 = Warrior("megaman", 1000)
    p2 = Wizard("Mago negro", 2500)

    p1.Attack(p2, 200)
    p2.Attack(p1, 1000)

    p1.Heal()
    p2.Heal()


if __name__ == "__main__":
    main()
