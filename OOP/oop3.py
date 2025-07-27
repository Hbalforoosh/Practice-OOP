class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}\nAge: {self.age}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def info(self):
        super().info()
        print(f"Subject: {self.subject}")


teacher1 = Teacher("ali", 35, "Mathematic")
teacher1.info()
