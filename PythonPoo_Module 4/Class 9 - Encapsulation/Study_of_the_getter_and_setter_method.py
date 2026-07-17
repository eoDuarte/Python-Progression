class Avaliation:
    def __init__(self, name, discipline, grade):
        self.name = name
        self.discipline = discipline
        self._grade = grade


    #Acess methods
    def get_grade(self): #getter Method
        return self._grade

    def set_grade(self, value): #setter Method
        if 0 <= value <= 10:
            self._grade = value
        else:
            print("Invalid grade")

