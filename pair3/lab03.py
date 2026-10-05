# 1

# text = input('enter text: ').lower()

# symbols = len(text)
# letters = 0
# numbers = 0
# spaces = 0
# vowel = 0
# words = len(text.split())
# golosni = 'аеиіїюяєоу'
# print(words)

# for ch in text:
#     if ch.isalpha():
#         letters += 1
#     if ch.isdigit():
#         numbers += 1
#     if ch == ' ':
#         spaces += 1
#     if ch in golosni:
#         vowel += 1

# print(f'Символів: {symbols} \nЛітер: {letters} \nЦифр: {numbers} \nПробілів: {spaces} \nГолосних: {vowel} \nСлів: {words}')

# 2

# full_name = input("enter your full name").lower().strip().title().split()
# first_name = full_name[1]
# last_name = full_name[0]
# patronymic = full_name[-1]

# print(f'{last_name} {first_name[0]}.{patronymic[0]}.')

#3

# first = input('enter first word: ').lower().replace(' ', '')
# second = input('enter second word: ').lower().replace(' ', '')

# if len(first) != len(second):
#     print('рядок не є анаграмою')
# else:
#     el = 0
#     for ch in first:
#         if ch in second:
#             second = second.replace(ch, '', 1)
#         else:
#             el = 1
#             print('рядок не є анаграмою')
#             break
#     if el != 1:
#         print('рядок є анаграмою')

#4

# text = input('enter text: ')
# normalized_text = text.lower().split()
# the_longest = normalized_text[0]
# the_shortest = normalized_text[0]
# unique = 0

# for el in normalized_text:
#     amount = 0

#     if len(the_longest) < len(el):
#         the_longest = el
#     if len(the_shortest) > len(el):
#         the_shortest = el

#     if normalized_text.count(el) > 1:
#         unique += 1 / normalized_text.count(el)
#     else:
#         unique += 1
    


   
# print(f"Найдовші: {the_longest} Найкоротші: {the_shortest} Унікальних слів: {int(unique)}")
        
# old_word = input('enter old word for replace: ')
# new_word = input('enter new word for replace: ')
# replaced_text = text.replace(old_word, new_word)

# print(f"normalized sentence - {replaced_text}")