from rich import print, inspect
from circle import Circle
from square import Square


def Main():

    ob1 = Circle(5)
    print(f"PERIMETER: {ob1.Perimeter():.1f}m")
    print(f"SQUARE AREA: {ob1.Square_area():.1f}m²")

    ob2 = Square(20)
    print(f"PERIMETER: {ob2.Perimeter():.1f}m")
    print(f"SQUARE AREA: {ob2.Square_area():.1f}m²")


if __name__ == "__main__":
    Main()
