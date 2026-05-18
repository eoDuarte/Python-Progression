from person import Person
class Student(Person):
    def __init__(self, name, age, course, group):
        super().__init__(name, age)
        self.course = course
        self.group = group

    def register(self):
        pass