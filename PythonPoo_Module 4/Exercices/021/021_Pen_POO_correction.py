'''This is a program that writes with the pen color the user chooses.'''
from rich import print


class Pen:
    def __init__(self, collor="blue"):
        choice = ""
        match collor.lower().strip():
            case "blue":
                choice = "[blue]"
            case "red":
                choice = "[red]"
            case "green":
                choice = "[green]"
            case _:
                choice = "[white]"
        self.collor = choice
        self.cover = True
    def write(self, msg):
        if self.cover:
            print(f":prohibited: the {self.collor}pen[/] is capped!")
        else:
            print(f"{self.collor}{msg}[/]", end=' ')

    def breake_line(self, amount=1):
        pass

    def cover(self):
        self.cover = True
    def uncover(self):
        self.cover = False

c1 = Pen("blue")
c2 = Pen("red")
c3 = Pen("green")

c1.uncover()
c2.uncover()

c1.write("hello world")
c2.write("work")

c3.write("Very good")