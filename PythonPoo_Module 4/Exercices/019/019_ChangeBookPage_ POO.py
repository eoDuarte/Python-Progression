#019 Create a book class that will simulate page turning.
# also considering if the user has reached the end of the book.

from rich import print
from rich.panel import Panel

class Book:
    def __init__(self, title, number_pages = 0):
        self.title = title
        self.number_pages = number_pages

    def __str__(self):
        return f"The chosen book was: {self.title} with {self.number_pages} pgaes."

    def Page(self):
        page = 0
        panel1 = Panel(f"Page: {page}",title=self.title, width=15, height=8)
        print(panel1)

        while page != -1:
            conteudo = f"Page: {page}"
            nextp = int(input("[6] = NEXT PAGE " "[4] = BACK PAGE " "[0] = CLOSE BOOK"
                              "\nR = "))
            if nextp == 6:
                page += 1
            if nextp == 4:
                page -= 1
            if nextp == 0:
                break

            panel = Panel(conteudo, title=self.title, width=15, height=8)
            print(panel)



l1 = Book("Harry poter", 3)
print(l1)
l1.Page()