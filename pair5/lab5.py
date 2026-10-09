import math

# # 1
# choice = input("введіть фігуру: ")

# if choice == 'прямокутник':

#     # обчислює площу прямокутника
#     def pryamokytnik_square(heigth = 0, width = 0):
#         return heigth * width
#     height = float(input('введіть висоту трикутника: '))
#     width = float(input('введіть ширину трикутника: '))
#     square = pryamokytnik_square(height, width)
#     print(f' площа прямокутника - {square}')

# if choice == 'коло' or choice == 'круг':
#     # обчислює площу кола
#     def circle_square(radius = 0):
#         return round(3.14159 * radius**2)
#     radius = float(input('Введіть радіус кола: '))
#     square = circle_square(radius)
#     print(f" площа кола - {square}")


# if choice == 'трикутник':
#     # обчислює трикутник за Героном
#     def trikutnik_square(first = 0,second = 0,third = 0):
#         half_p = (first + second + third) / 2
#         square_trikytnik = round(math.sqrt(half_p * (half_p - first) * (half_p - second) * (half_p - third)), 2)
#         return square_trikytnik
#     first = float(input('Введіть першу сторону: '))
#     second = float(input('Введіть другу сторону: '))
#     third = float(input('Введіть третю сторону: '))
#     square = trikutnik_square(first, second, third)
#     print(f'площа = {square}')

# 2

# number = int(input('Enter number: '))


# def is_prime(n):
#     sum = 0
#     for i in range(1,n + 1):
#         if n % i == 0:
#             sum += 1

#     if sum > 2 or n == 1:
#         return 'ні'
#     return 'так' 

# def divisors(n):
#     arr = []
#     for i in range(1,n + 1):
#             if n % i == 0:
#                 arr.append(i)
#     return arr

# def digit_sum(n):
#     sum = 0
#     normalized_n = str(n)
#     for ch in normalized_n:   
#         sum += int(ch)
#     return sum


# answer_prime = is_prime(number)
# answer_divisors = divisors(number)
# answer_sum = digit_sum(number)

# print(f"Просте число: {answer_prime}\nДільники: {answer_divisors}\nСума цифр: {answer_sum}")

#3

# marks = [1,2, 5, 10, 12]

# value = input('Введіть поріг: ')

# def average(grades):
#     return round((sum(grades) / len(grades)), 1)

# def minimum(grades):
#     return min(grades)

# def maximum(grades):
#     return max(grades)

# def count_above(grades, value):
#     sum = 0
#     for grade in grades:
#         if grade > float(value):
#             sum += 1
#     return sum

# answer_average = average(marks)
# answer_min = minimum(marks)
# answer_max = maximum(marks)
# answer_count_above = count_above(marks, value)

# print(f"Середній бал: {answer_average}\nМінімальна: {answer_min}\nМаксимальна: {answer_max}\nВище 9: {answer_count_above}")

#4

password = input("Enter password: ")
problems = []

def min_length(text):
    if len(text) >= 8:
        return True
    problems.append('пароль не містить 8 символів')
    return False

def is_has_number(text):
    for i in text:
        if i.isdigit():
            return True
    problems.append('пароль не містить числа')
    return False

def is_has_upperCase(text):
    for i in text:
        if i.isupper():
            return True
    problems.append('пароль не містить високого регістру')
    return False

def is_has_lowerCase(text):
    for i in text:
        if i.islower():
            return True
    problems.append('пароль не містить нижнього регістру')
    return False

def is_has_specific(text):
    for i in text:
        if i.lower() == i.upper() and i != ' ' and not i.isdigit():
            return True
    problems.append('пароль не містить спец символів')
    return False

answer_min_len = min_length(password)
answer_has_number = is_has_number(password)
answer_has_upper = is_has_upperCase(password)
answer_has_lower = is_has_lowerCase(password)
answer_has_spec = is_has_specific(password)

if answer_min_len and answer_has_number and answer_has_upper and answer_has_lower and answer_has_spec:
    print('Пароль надійний')
else:
    print(f"Пароль не надійний \nНе виконано: {' ,'.join(problems)}")


