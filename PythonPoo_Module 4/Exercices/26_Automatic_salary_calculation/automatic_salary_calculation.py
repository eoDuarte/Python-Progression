from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print

class Employee(ABC):
    def __init__(self, name=""):
        self.gross_salary = 0
        self.salary = 0
        self.name = name

    minimum_wege = 1612
    inss = 7.5

    @abstractmethod
    def salary_calc(self):
        pass

    def salary_analysis(self):
        mensage = f"{self.name}'s salary is {self.salary} and corresponds to {self.salary / 1612:.1f} minimum wages."
        panel = Panel(mensage, title="Salary Analysis", width=50)
        print(panel)


class Hourly(Employee):
    def __init__(self, name="", hour_value=0, work_hour=0):
        super().__init__(name)
        self.hour_value = hour_value
        self.work_hour = work_hour
        self.gross_salary = self.work_hour * self.hour_value

    def salary_calc(self):
        discount = self.gross_salary * Employee.inss / 100
        self.salary = self.gross_salary - discount
        return self.salary


class Monthly(Employee):
    def __init__(self, name="", month_payment=0):
        super().__init__(name)
        self.month_payment = month_payment
        self.gross_salary = self.month_payment

    def salary_calc(self):
        discount = self.gross_salary * Employee.inss / 100
        self.salary = self.gross_salary - discount
        return self.salary
