
class Thermostat:
    def __init__(self, temperatura=24):
        self.__temperatura = temperatura


    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, value):
        if value % 0.5 != 0:
            raise ValueError(f"ERROR: the temperature {value}ºC is invalid")

        if value < 16:
            self.__temperatura = 16
        elif value > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = value

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}ºC"









