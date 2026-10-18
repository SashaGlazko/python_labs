import os

#1

# try:
#     a = float(input('введіть перше число: '))
#     b = float(input('введіть друге число: '))
#     operation = input("введіть операцію: ")
#     res = 0

# # використовую технологію switch case яку вже знаю з js і яка розрахована на виконання таких завдань щоб не писати мільйон строчок з if else, тому не баньте.Дякую
#     match operation:
#         case '*':
#             res = a * b
#         case '/':
#             res = a / b
#         case '-':
#             res = a + b
#         case '-':
#             res = a - b
# except ZeroDivisionError:
#     print('ділення на 0')
# except ValueError:
#     print('введіть числа коррекно')
# else:
#     print(f'{res} - result')

#2

# def input_grade():
#     while True:
#         try:
#             res = int(input("Введіть оцінку 1...12: "))
#             if res < 1 or res > 12:
#                 raise ValueError('Введіть число від 1 до 12!')
#             return res
#         except ValueError as e:
#             print(f'{e}')

# print(input_grade())

# 3

# students = ['Sanya','Ivan','Goga','Misha']
# marks = {
#     'Math': 12,
#     'It':12,
#     'PE': 2,
# }
# while True:
#     try:
#         choose = int(input('Виберіть тип пошуку: 1;2: '))
#         if choose != 1 and choose != 2:
#             raise ValueError('ви обрали значеня не з доступного діапазону')
            
#         if choose == 1:
#             print(f'\n {students}')
#             index = int(input('Введіть індекс студента: '))
#             print(students[index])
#             break
#         if choose == 2:
#             print(f'\n {marks}')
#             subject = input('Введіть назву предмета: ')
#             mark = marks[subject]
#             print(mark)
#             continue
#     except IndexError:
#         print('Немає такого студента')
#     except KeyError:
#         print('Немає такої оцінки')
#     except ValueError as v:
#         print(v)

# 4
info = []
falsy = 0
problems = {}
truly = 0
last_key = -1
separator = ';'
try:
    with open('students.txt', 'r', encoding='utf-8') as file:
        for index,line in enumerate(file, start=1):
            try:
                arr = line.strip().split(separator)

                last_key = index
                if separator not in line:
                    falsy += 1
                    raise ValueError('у рядку немає роздільника «;»')
                if len(arr) != 2:
                    falsy += 1
                    raise ValueError('кількість полів неправильна')
                if not arr[1].isdigit():
                    falsy += 1
                    raise ValueError('оцінка не ціла')
                if 0 > int(arr[1]) or int(arr[1]) > 100:
                    falsy += 1
                    raise ValueError('бал не в межі діапазону')
                truly += 1
                info.append([int(arr[1]),arr[0]])
            except ValueError as v:
                problems[last_key] = str(v)
except FileNotFoundError as f:
    falsy += 1
    problems[last_key] = 'файл відсутній'

info.sort(reverse=True)

for key in problems.keys():
    print(f"Рядок {key} пропущено: {problems[key]}")
print(f'Правильних записів: {truly}')
print(f'Пропущено: {falsy}')

with open('report.txt', 'w', encoding='utf-8') as file:
    for el in info:
        file.write(f'{el[1]};{el[0]}\n')
print('Створено report.txt')