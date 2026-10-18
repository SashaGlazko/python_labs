# if 7 > 5 синтаксична помилка коли неправильно записуємо щось
#     print('ok')

# n = int("Number")
# print(n) Value error помилка в конвертації даних


# # як if else тільки саме для помилок
# try:
#     age = int(input("age: "))
#     print(age)
# except ValueError:
#     print("Enter valid age")
# # ValueError - коли тип операції правильний, а значення використати неможна

# try:
#     a = int(input("a: "))
#     b = int(input("a: "))
#     res = a / b 
#     print(res)
# except ValueError:
#     print('a, b - might be nubers')
# except ZeroDivisionError:
#     print('b cannot be 0')
# finally:
#     print('Програму завершено')

# try:
#     grade = int(input("Enter your grade:"))
#     if 1 > grade or grade >= 12:
#         raise ValueError("Grade must be between 1 and 12")
#     print(f'your grade is {grade}')
# except ValueError as error_limit:
#     print(f'Error: {error_limit}')

# while True:
#     try:
#         grade = int(input("Enter your grade:"))
#         if 1 > grade or grade >= 12:
#             raise ValueError("Grade must be between 1 and 12")
#         print(f'your grade is {grade}')
#         break
#     except ValueError as error_limit:
#         print(f'Error: {error_limit}')
    
# def int_input(message):
#     while True:
#         try:
#             return int(input(message))
#         except ValueError:
#             print('Please enter an integer.')
# n = int_input('Pleade inter a number: ')
# print(n)

# def input_grade():
#     while True:
#         try:
#             grade = int(input("Enter your grade 1...12: "))
#             if grade < 1 or grade > 12:
#                 raise ValueError("Grade must be between 1 and 12 ")
#             return grade
#         except ValueError as error:
#             print(error)
# grade = input_grade()
# print(f'Оцінка {grade} прийнята: ')

# price = {
#     "apple": 10,
#     "banana": 20,
# }
# product = input()

# try:
#     print(price[product])
# except:
#     print(f"prroduct is not fundf")

# product = price.get(product, 'не знайдено')

# try:
#     with open('data.txt', 'r', encoding="utf-8") as f:
#         data = f.read()
#         print(data)
# except FileNotFoundError:
#     print('Такого файлу немає')

line = 'Ivan;95'
parts = line.strip().split(';')
if len(parts) != 2:
    print('Помилка у рядку')
else:
    name = parts[0]
    grade = parts[1]

    try:
        grade_int = int(grade)

        if grade_int < 0 or grade_int > 100:
            raise ValueError('Бал не від 1 до 100')
    except ValueError as e:
        print(f'Помилка {e}')
    else:
        print(f"Правильний запис: {name} - {grade_int}")

# lines = [
#     "Ivan;95",
#     "Liza;hello",
#     "Vadymka;100"
# ]

# for line_number,line in enumerate(lines, start=1):
#     parts = line.strip().split(';')
#     if len(parts) != 2:
#         print(f"Рядок {line_number} має помилку")
#         continue
#     name = parts[0]
#     try:
#         score = int(parts[1])
#     except ValueError:
#         print(f'Рядок {line_number} пропущено, бал виставлений не правильно')
#         continue
# print(f'Правильний запис {name} - {score}')