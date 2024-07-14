class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def print_name(self):
        print(self.firstName, self.lastName)


class Student(Person):
    # pass
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = 2022

    def __str__(self):
        return f"{self.firstName} {self.lastName} graduated in {self.graduationYear}"


x = Student("Joe", "Doe", 2019)
print(x)
