from rich import print, inspect
from person import Person
from student import Student
from teacher import Teacher
from employee import Employee


def main():
    a1 = Student("José", 17, "informatic", "T01")
    a1.have_a_birthday()
    a1.to_study()
    inspect(a1, methods=True)


if __name__ == "__main__":
    main()