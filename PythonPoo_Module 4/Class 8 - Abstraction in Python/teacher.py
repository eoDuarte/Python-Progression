from person import Person
class Teacher(Person):

    def to_study(self):
        pass

    def __init__(self, name, age, specialty, level):
        super().__init__(name, age)
        self.specialty = specialty
        self.level = level

    def teach(self):
        pass