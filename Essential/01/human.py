class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info(self):
        print(self.name, "is", self.age)

john = Human("John", 22)

mary = Human("Mary", 20)

print(john.name, "is", john.age)
print(mary.name, "is", mary.age)

Human.print_info(john)
Human.print_info(mary)

john.print_info()
mary.print_info()

peter = Human("Peter", 30)

peter.print_info()
