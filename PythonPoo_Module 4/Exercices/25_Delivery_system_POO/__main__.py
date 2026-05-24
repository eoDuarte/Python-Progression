from rich import print, inspect
from rich.table import Table
from transport import *


def main():
    dist = 80
    types_delivery = [Motorbike(dist), Truck(dist), Drone(dist)]
    '''delivery = Drone(dist)
    print(f"{type(delivery).__name__} delivery {dist}Km = {delivery.Delivery_calculate()}")'''

    table = Table(title="Delivery table")
    table.add_column("Distance")
    table.add_column("Type")
    table.add_column("Delivery")


    for item in types_delivery:
        table.add_row(f"{dist}Km", f"{type(item).__name__}", f"{item.Delivery_calculate()}")
    print(table)
if __name__ == "__main__":
    main()
