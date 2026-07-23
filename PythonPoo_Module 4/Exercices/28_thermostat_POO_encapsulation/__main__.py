from Thermostat import Thermostat
from rich import inspect
def main():
    t = Thermostat()
    t.temperatura = 25.5
    print(t.ftemperatura)
    inspect(t, private=True)


if __name__ == "__main__":
    main()