from abc import ABC,abstractmethod

class Hotdrinks(ABC):

    def Prepare(self):
        print("-----Preparing-----")
        self.boil_water()
        self.Mix()
        self.Server()
        print("____Drink ready-----\n")

    def boil_water(self):
        print("1.Boiling water in 100 degrees")

    @abstractmethod
    def Mix(self):
        pass

    @abstractmethod
    def Server(self):
        pass


class Coffee(Hotdrinks):
    def Mix(self):
        print("2.passing pre-pressurized water through ground coffee.")
    def Server(self):
        print("3.Serving in a small cup.")


class Tea(Hotdrinks):
    def Mix(self):
        print("2.dipping the sachet in the water")

    def Server(self):
        print("3.served in a mug with lemon.")


class Milk(Hotdrinks):
    def Mix(self):
        print("2.passing pressurized water through the milk spout")

    def Server(self):
        print("3.serving with the large mug already filled with coffee.")
