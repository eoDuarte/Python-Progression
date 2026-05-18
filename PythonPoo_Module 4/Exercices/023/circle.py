from polygon import Polygon


class Circle(Polygon):
    def __init__(self, side_radius):
        super().__init__(side_radius)

    def Perimeter(self):
        return 2 * 3.14 * self.side_radius

    def Square_area(self):
        return 3.14 * (self.side_radius * self.side_radius)
