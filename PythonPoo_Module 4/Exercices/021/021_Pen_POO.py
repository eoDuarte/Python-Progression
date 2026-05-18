#Create a class called "pen" that simulates the functioning of a colored pen,
# capable of writing sentences in relative terms.
from rich import print


class Pen:
    def __init__(self, write):
        self.write = write
        print(f" Your frase is: {self.write}")

    def colorselect(self):
        cor = int(input("Please select one color: [1]Blue [2]Red [3]Yellow"
                    "\nAnswer: "))
        if cor ==1:
            print(f"[blue]{self.write}[/]")
        if cor == 2:
            print(f"[red]{self.write}[/]")
        if cor == 3:
            print(f"[yellow]{self.write}[/]")
        else:
            print(f"You didn't chooce any collor")


w1 = Pen("Escolhendo uma cor")
w1.colorselect()


