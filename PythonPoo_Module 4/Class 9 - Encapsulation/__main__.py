from Study_of_the_getter_and_setter_method import Avaliation
from rich import print, inspect
def main():
    a = Avaliation("Pedro", "Math", 8.5)
    a.set_grade(923)
    inspect(a, private=True)

if __name__ == "__main__":
    main()
