#019 Create a book class that will simulate page turning.
# also considering if the user has reached the end of the book.
from rich import print
import time
class Book:

    def __init__(self, title, page):
        self.title = title
        self.page = page
        self.current_page = 1

        print(f":open_book:[blue] You open the book[red] {self.title}[/] with {self.page} pages."
              f"You are now on the page [yellow]{self.current_page}[/][/blue]")

    def advance_page(self, amount):
        count = 0
        for pg in range(0, amount, 1):
            if not self.end_of_the_book():
                self.current_page +=1
                print(f"Page{self.current_page} :arrow_forward: ", end='')
                time.sleep(0.3)
                count +=1
        print(f"[blue]You have advanced {count} and you are now on page [yellow]{self.current_page}[/][/blue]")
        if self.end_of_the_book():
            print(f":close_book:[red]You have reached the end of the book {self.title}")
    def end_of_the_book(self) -> bool:
        return True if self.current_page == self.page else False

l1 = Book("Harry Potter", 20)
l1.advance_page(10)
l1.advance_page(20)
l1.advance_page(10)
l1.advance_page(50)