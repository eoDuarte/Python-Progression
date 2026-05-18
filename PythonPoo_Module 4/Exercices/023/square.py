from polygon import Polygon


class Square(Polygon):
    def __init__(self, side_radius):
        super().__init__(side_radius)

    def Perimeter(self):
        return self.side_radius * 4

    def Square_area(self):
        return self.side_radius * self.side_radius
