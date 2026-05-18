from person import Person


class Student(Person):
    def to_study(self):
        print(f"{self.name} is studying {self.course} in the class {self.group}")

    def __init__(self, name, age, course, group):
        super().__init__(name, age)
        self.course = course
        self.group = group

    def register(self):
        pass
