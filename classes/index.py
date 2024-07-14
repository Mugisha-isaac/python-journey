class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # string representation
    def __str__(self):
        return f"{self.name} ({self.age})"


p1 = Person("John", 18)
print(p1)
# print(p1.name)
# print(p1.age)
