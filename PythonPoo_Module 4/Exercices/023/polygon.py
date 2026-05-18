from abc import ABC, abstractmethod


class Polygon(ABC):
    side_radius: int

    def __init__(self, side_radius=0):
        self.side_radius = side_radius

    @abstractmethod
    def Perimeter(self):
        pass

    @abstractmethod
    def Square_area(self):
        pass
