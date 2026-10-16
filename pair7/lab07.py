import os

# 1
# sum_of_lines = 0
# sum_of_sumbols = 0
# sum_of_words = 0
# max_in_line = [0, None, 'for text']
# with open('text.txt', 'r', encoding='utf-8') as file:
#     for index, line in enumerate(file, start = 1):
        
#         sum_of_lines += 1
#         arr_line = line.strip().split()
#         sum_of_words += len(arr_line)
        
#         sumbols_in_line = ''.join(arr_line)
#         if len(sumbols_in_line) > max_in_line[0]:
#             max_in_line[0] = len(sumbols_in_line)
#             max_in_line[1] = index
#             max_in_line[2] = line
            

#         for part in arr_line:
#             sum_of_sumbols += len(part)
# print(f"Рядків: {sum_of_lines}\nСлів: {sum_of_words}\nСимволів {sum_of_sumbols}\n"+
#       f"Найдовший рядок: No{max_in_line[1]}, {max_in_line[0]}символів \n Текст: {max_in_line[2]}")

# 2
# obj = {}
# fragment = input('Enter fragment: ')
# with open('text.txt', 'r', encoding='utf-8') as file:
#     for index, line in enumerate(file, start = 1):
#         if fragment.lower() in line.lower():
#             obj[index] = line
#     if not obj:
#         print("not found coincidences")
#     else:
#         print('coincidences -', obj)

#3

# students = {}
# with open('students.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         parts = line.strip().split(';')
#         if int(parts[1]) > 80:
#             students[parts[0]] = int(parts[1])
# sorted_students = sorted((students.items()), reverse= True)

# with open('result.txt', 'w', encoding='utf-8') as file:
#     for student in sorted_students:
#         file.write(f"{student[0]};{student[1]}\n")

#4 

students = {}
result = []
the_biggest_average = 0
with open('grades.csv', 'r', encoding='utf-8') as file:
    for line in file:
        info = line.strip().split(';')
        if not students.get(info[0]):
            students[info[0]] = [[info[1],int(info[2])]]
        else:
            students[info[0]].append([info[1],int(info[2])])
# print(students)
with open('report.txt', 'w', encoding='utf-8') as file:
    for name in students.keys():
        average = 0
        marks = []
        for arr in students[name]:
            marks.append(arr[1])
            average = sum(marks) / len(marks)
            if the_biggest_average < average:
                the_biggest_average = average

        result.append((average,name,len(marks)))
    
    result.sort()
    botanics = []
    for part in result:
        file.write(f"{part[1]} - оцінок: {part[2]} - середній: {round(part[0], 2)}\n")
        if part[0] == the_biggest_average:
            botanics.append(part[1])
    file.write(f"найкращий результат: {botanics} - {the_biggest_average}")

