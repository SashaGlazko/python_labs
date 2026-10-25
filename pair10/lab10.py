#1

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         return f"name {self.name}"


# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group

#     def info(self):
#         return f"mate: {self.name}, group: {self.group}"


#2 

# class Person:
#     def __init__(self, name):
#         self.name = name


#     def info(self):
#         return f"name {self.name}"


# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group

#     def info(self):
#         return f"kid: {self.name}, group: {self.group}"

# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject

#     def info(self):
#         return f"Teacher: {self.name}, lesson: {self.subject}"

# people = [
#     Student("Volodya Mahno", "IT10"),
#     Person("misha kalinovski"),
#     Student("mishka bratishka", "11"),
#     Teacher("Olena Kovalenko", "Python")
# ]
# for person in people:
#     print(person.info())

#3
class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        for s in self.students:
            if s.name == student.name:
                return
        self.students.append(student)

    def remove(self, name):
        new = []
        for student in self.students:
            if student.name != name:
                new.append(student)
        self.students = new

    def show(self):
        print(f"course {self.title}")
        print(f"teacher {self.teacher.name} subj {self.teacher.subject}")
        print("Студенти:")
        if not self.students:
            print("empty")
        else:
            for i, student in enumerate(self.students, 1):
                print(f"{i}. {student.name}, group {student.group}")

class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"name {self.name}"


class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

    def info(self):
        return f"mate {self.name}, goup {self.group}"


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def info(self):
        return f"teacher {self.name}, subj {self.subject}"

teacher1 = Teacher("Bim bom", "Python")
python_course = Course("Python", teacher1)
s1 = Student("miha pups", "IT7")
s2 = Student("anton A1 mini", "IT1")
s3 = Student("dima p1s", "IT2")
s4 = Student("opel p2s", "IT2")
python_course.add_student(s1)
python_course.add_student(s2)
python_course.add_student(s3)
python_course.add_student(s4)
python_course.add_student(s1) 
python_course.show()
python_course.remove("Mia maievska")
python_course.show()