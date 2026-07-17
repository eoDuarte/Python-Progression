from Study_of_the_property import Avaliation
from rich import print, inspect
def main():
    a = Avaliation("Pedro", "Math", 8.5)
    a.grade = -7.2
    inspect(a, private=True)

if __name__ == "__main__":
    main()
