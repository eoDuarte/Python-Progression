from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, distance=0):
        self.distance = distance
        self.delivery = 0

    @abstractmethod
    def Delivery_calculate(self):
        pass


class Motorbike(Transport):
    factor = .5

    def __init__(self, distance):
        super().__init__(distance)

    def Delivery_calculate(self):
        self.delivery = self.distance * Motorbike.factor
        return f"£{self.delivery:.2f}"


class Truck(Transport):
    factor = 1.2

    def __init__(self, distance):
        super().__init__(distance)

    def Delivery_calculate(self):
        if self.distance < 50:
            return f"Only over 50Km"
        else:
            self.delivery = self.distance * Truck.factor
            return f"£{self.delivery:.2f}"


class Drone(Transport):
    factor = 9.5

    def __init__(self, distance):
        super().__init__(distance)

    def Delivery_calculate(self):
        if self.distance > 10:
            return f"Only under 10Km"
        else:
            self.delivery = self.distance * Drone.factor
            return f"£{self.delivery:.2f}"
