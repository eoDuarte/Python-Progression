class Avaliation:
    def __init__(self, name, discipline, grade):
        self.name = name
        self.discipline = discipline
        self._grade = grade


    @property
    def grade(self): #getter
        return self._grade

    @grade.setter
    def grade(self,value):
        if 0 <= value <= 10:
            self._grade = value
        else:
            print("Invalid grade")
