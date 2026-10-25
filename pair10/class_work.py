class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f'Name: {self.name}'
class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
    def info(self):
        return f'Name: {self.name}, Group: {self.group}'
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def info(self):
        return f'Name: {self.name}, Group: {self.subject}'


# person1 = Person("John")
# student = Student("Liza", "10IT")
people = [Person("Vadym"), Student('Liza', '10IT'), Teacher("Ivav", "IT")]

for person in people:
    print(person.info())
person2 = Person("Vadym")


print(isinstance(person2, Student))
# print(person1.info())
# print(student.info())