# #1

# class Rectangle:
#     def __init__(self, width, heigth):
#         self.width = width
#         self.heigth = heigth

#     def area(self):
#         return self.width * self.heigth
     
#     def perimeter(self):
#         return 2 * (self.width + self.heigth)
    
#     def perimeter(self):
#         return 2 * (self.width + self.heigth)

#     def info(self):
#         print(f"width = {self.width} heigth = {self.heigth}")

#         print('P = ', self.perimeter()) 
#         print('S = ', self.area()) 

# 2

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = []
#         for grade in grades:
#             self.add_grade(grade)

#     def add_grade(self, grade):
#         if 1 <= grade <= 12:
#             self.grades.append(grade)

#     def average(self):
#         try:
#             average = self.average = sum(self.grades) / len(self.grades)
#         except ZeroDivisionError:
#             average = '0'
#         return average

#     def __str__(self):
#         return f"ПІБ - {self.name},оцінки - {self.grades}, середнє - {self.average()}"
# stud1 = Student('anna', [32])
# print(stud1)

#3 

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = []
#         for grade in grades:
#             self.add_grade(grade)

#     def add_grade(self, grade):
#         if 1 <= grade <= 12:
#             self.grades.append(grade)

#     def average(self):
#         try:
#             aver =sum(self.grades) / len(self.grades)
#         except ZeroDivisionError:
#             aver = 0
#         return aver

#     def __str__(self):
#         return f"ПІБ - {self.name},оцінки - {self.grades}, середнє - {self.average()}"
# stud1 = Student('anna', [32])
# print(stud1)

# students = [
#     Student("Vasya", [12, 12, 12]),
#     Student("Yanucovich", [9, 9, 12]),
#     Student("Uschenko", [2, 69, 1]),
#     Student("Zelenskiy", [14, 8, 8]),
#     Student("Kutchma", [6, 6, 6,6, 7,7,7])]
# max_avg = 0
# top_students = []

# for student in students:
#     print(f"{student.name} — {student.grades}")

# for student in students:
#     if student.average() > max_avg:
#         max_avg = student.average()

# for student in students:
#     if student.average() == max_avg:
#         top_students.append(student)

# print(f"the best average: {max_avg}")
# for student in top_students:
#     print(f" {student.name} average: {student.average()})")


#4
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.vlasnyk = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("must be more than 0")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print(f"must be more than 0")
        elif amount > self.balance:
            print(f"not enough money -{amount}")
        else:
            self.balance -= amount

    def info(self):
        print(f"{self.vlasnyk}: bal {self.balance}")


man = BankAccount("Man", 1000)
woman = BankAccount("Woman", 700)

man.deposit(500) 
man.withdraw(300)
man.withdraw(2000)

woman.withdraw(200)
woman.deposit(100)

man.info()
woman.info()