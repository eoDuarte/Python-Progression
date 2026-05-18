class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def have_a_birthday(self):
        self.age += 1