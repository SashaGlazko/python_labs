import os

if not os.path.exists('text.txt'):
    with open('text.txt', 'w', encoding="utf-8") as file:
        file.write("Python - популярна мова програмування.\n")
        file.write("Python використовується для роботи з даними.\n")
        file.write("Файли дозволяють зберігати інформацію\n")
        file.write("Python вимагає практики.\n")
        file.write("Сьогодні ми працюємо з текстовими файлами.\n")

if not os.path.exists('numbers.txt'):
    with open('numbers.txt', 'w', encoding="utf-8") as file:
        file.write("12\n8\n25\n4\n16\n")

if not os.path.exists('students.txt'):
    with open('students.txt', 'w', encoding="utf-8") as file:
        file.write("Ivanenko Anna;91\n")
        file.write("Leshchenko Ivan;76\n")
        file.write("Komarova Sophie;97\n")
        file.write("Bondarenko Illya;84\n")

if not os.path.exists('grades.csv'):
    with open('grades.csv', 'w', encoding="utf-8") as file:
        file.write("Anna;Python;11\n")
        file.write("Anna;Math;10\n")
        file.write("Ivan;Python;6\n")
        file.write("Ivan;Math;5\n")
        file.write("Sophie;Python;11\n")
        file.write("Sophie;Math;12\n")
        file.write("Illya;Python;9\n")
        file.write("Illya;Math;8\n")

with open('hello.txt','w', encoding='utf-8') as file:
    file.write('Hello world!\n')

# with - команда яка автоматично закриває файл після завершення роботи з ним
# open - відкриває файл(функція)
# 1 параметр - шлях з назвою файла(з яким файлом ми працюємо) - відносне або загальне посилання
# 2 параметр - 'W' режими для доступу файлів
# w - режим запису.Якщо файл вже існує, то його зміст перезапишеться
# r - читає файли але при умові, що такий файл вже існує.Інакше - помилка
# a - додає в кінець і старий вміст не зтирається.Додає до записаного інфу.Якщо файла немає, то створить його
# x - створює новий файл.Якщо існує такий файл, то помилка
# 3 параметр - кодування. треба utf-8, щоб було зрозуміло кириллицю програмі 
# as file - додає псевдонім всьому записаному вище.
# далі метод або .write() або .read()
# with open('text.txt','r', encoding='utf-8') as file:
#     text = file.read()
# print(f"read() => {text}, len = {len(text)}")

# with open('text.txt','r', encoding='utf-8') as file:
#     line1 = file.readline()
#     other_lines = file.readlines() # всі строки незчитані зчитує
#     line2 = file.readline()
# print(line1)
# print(other_lines)
# print(line2)

# with open('text.txt','r', encoding='utf-8') as file:
#     other_lines = file.readlines()
# for line in lines:
#     print(line)

# with open('text.txt','r', encoding='utf-8') as file:
#     for number, line in enumerate(file, start = 1): # який файл перебираємо, і перебираємо номер строки за ітераціями
#         clean_line = line.strip()
#         print(f" {number}. {clean_line}")

# line = 'Komarov Ivan;2\n'
# clean_line = line.strip()
# name, grade = clean_line.split(';')
# print(name)
# print(grade)

# students = []
# botanics = []

# with open('students.txt', 'r', encoding = 'utf-8') as file:
#     for line in file:
#         name, grade = line.strip().split(';')
#         students.append([name,grade])
#         if int(grade) >= 90:
#             botanics.append([name, grade])
#     print(students)
#     print(botanics)
# with open('botanics.txt', 'w', encoding = 'utf-8') as file:
#     for name, grade in botanics:
#         file.write(name + ';' + grade + '\n')


# grades = []
# with open('grades.csv', 'r', encoding='utf-8') as file:
#     for line in file:
#         name,subject,grade = line.strip().split(';')
#         grades.append(int(grade))
#         print(f"{name};{subject};{grade}")
# average = sum(grades) / len(grades)

