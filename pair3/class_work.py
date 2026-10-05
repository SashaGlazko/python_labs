# name = "Oleksandr"
# age = '18'
# print(len(name)) # визначає к-сть символів
# print(name[0])# O
# print(name[9])# помилка
# print(name[len(name) - 1])

# text = input()
# if len(text) > 0:
#     print(text[0])
# else:
#     print('рядок порожній')

# text = 'hello world'
# print(text[:5]) # зріз від 0 до 5 не включно
# print(text[6:]) # зріз від 6 до кінця
# print(text[::2]) # step через 1
# print(text[::-1]) # ззаду наперед
# string тип - незмінна колкція
# text[1] = 3 - не можна так робити

# print(text.upper()) # робить caps
# text_upper = text.upper()
# print(text.lower()) # робить маленькими
# print(text.title()) # кожне нове слово з великої
# print(text.capitalize()) # речення з великої літери(1 буква)

# text = '    Python    '
# print(text.lstrip()) # зліва видалити пробіли
# print(text.rstrip()) # зправа видалити пробіли
# print(text.strip()) # видалити пробіли по бокам


# user_login = 'admin'

# login = input('enter your login: ').lower().strip() # нормалізація тексту

# if user_login == login:
#     print('Welcome')

# password = input()
# digits = 0
# u_letter = 0
# if len(password) >= 8:
#     for char in password: # хочемо вивести кожен символ окремо
#         if char.isdigit(): # перевірка на число
#             digits += 1
#         if char.isupper(): # перевірка на капс
#             u_letter += 1
#     if digits >= 2 and u_letter >= 2:
#         print('надійний')
#     else:
#         print("не надійний")
# else:
#     print('пароль повинен мати більше 8 символів')

# password.isdigit() # чи число  
# password.isupper() # чи капс
# password.islower() # чи маленькі літери
# password.isalpha() # чи букви
# password.isalnum() # чи складається виключо з букв та цифр

# golosni = 'аеиоуїюя'
# text = input('').lower()
# count = 0

# for char in text:
#     if char in golosni:
#         count += 1
# print(count)

# text = "Hello World! Python is the best!!"
# words = text.split() # перетворює на список
# print(words)
# result = "-".join(words) # обернене до split
# print(result)

# new_text = text.replace('Tython', "Javascript") # міняє частини
# print()

# text = input().lower().strip()

# if text() == text[::-1]: #Дід Око
#     print('palindrom')
# else:
#     print('not palindrom')

text = input().strip()

words = text.split()
max_word = words[0]

for word in words:
    if len(word) > len(max_word):
        max_word = word
print(max_word, type(max_word))