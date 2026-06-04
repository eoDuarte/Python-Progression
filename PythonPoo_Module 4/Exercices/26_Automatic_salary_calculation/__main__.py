from automatic_salary_calculation import *
from rich import inspect


def main():
    worker1 = Hourly("leo", 75, 100)
    worker1.salary_calc()
    worker1.salary_analysis()

    worker2 = Monthly("Renée", 5000)
    worker2.salary_calc()
    worker2.salary_analysis()


if __name__ == "__main__":
    main()
