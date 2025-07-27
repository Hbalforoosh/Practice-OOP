class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def is_successful(self):
        return self.average() >= 12


student1 = Student("ali", [20, 18, 15])
student2 = Student("Hosein", [10, 8, 12])

print(
    f"{student1.name} average: {student1.average()} | Successful:{student1.is_successful()}\n"
)
print(
    f"{student2.name} average: {student2.average()} | Successful:{student2.is_successful()}\n"
)
