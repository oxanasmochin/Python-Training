class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self) :
        return sum(self.marks)/len(self.marks)

    def goto_school(self) :
        print("Im going to {} school.".format(self.school))

anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(44)
print(anna.marks)

print(anna.average())
anna.goto_school()
