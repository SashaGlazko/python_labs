# 1
# arr = [12, 3, 4, 14, -12, 5, 10, 16, -4]
# positive_arr = []
# negative_arr = []
# even_arr = []
# kratni_3_arr = []
# minimum = min(arr)
# maximum = max(arr)
# suma = sum(arr)
# average = round(suma / len(arr), 2)

# for el in arr:
#     if el > 0:
#         positive_arr.append(el)
#     else:
#         negative_arr.append(el)
#     if el % 2 == 0:
#         even_arr.append(el)
#     if el % 3 == 0:
#         kratni_3_arr.append(el)


# print(f"Додатні:{positive_arr}\nВід'ємні:{negative_arr}\nПарні:{even_arr} \nКратні 3:{kratni_3_arr}\nMin:{minimum}; Max:{maximum}; Sum:{suma}; Average:{average}")

#2

# group1 = {'Anna','Ivan','Olha'}
# group2 = {'Ivan','Maksym','Olha'}
# everybody = group1 | group2
# spilni = group1 & group2
# unique_first = group1 - group2
# unique_second = group2 - group1
# vsi_unikalni = unique_first | unique_second
# print(f"Спільні:{spilni}\nТільки group1:{unique_first}\nТільки group2:{unique_second}\nУсі:{everybody}\nУсі унікальні:{vsi_unikalni}\n")

# 3

# products = {
#     "milk": 50,
#     "bread": 40,
#     "carrot": 60,
#     "potato": 27
# }

# choose = input("Ви хочете змінити вартість товару чи додати новий? \n [вартість] або [новий] або [перебрати товари] - ")

# if choose == 'вартість':
#     print(products)

#     choose_key = input("оберіть, ціну ЯКОГО товару ви хочете змінити - ").lower().strip()
    
#     key = products.get(choose_key, 'Немає такого товару.Виконайте програму ще раз.')
#     if choose_key not in products:
#         print(key)
#     else:
#         new_price = input('Введіть нову ціну товару - ').strip()
#         products[choose_key] = new_price
#         print(f'ціна товару {choose_key} була змінена на {new_price}')
#         print(products)
# elif choose == 'новий':
#     print(products)
#     new_property = input('введіть назву нового товару - ')
#     new_key = input(f'введіть ціну товару {new_property} - ')
#     products[new_property] = new_key
#     print(f"Вітаю, ви додали новий товар {new_property}\n",products)
# elif choose == 'перебрати товари':
#     for property, key in products.items():
#         print(f"{property}: {key}")
# else:
#     print('Ви ввели некоректну опцію')

#4

name = input('введіть назву групи для нового журналу - ').strip()
year = input('ведіть навчальний рік у форматі [2026/2027] - ').strip()

rate = {} # заглушка для 'за середнім' та 'найвищ'
journal = dict()
journal['group_info'] = (name, year)
print(journal)

while True:
    choose = input(
        '\nвведіть функцію, яку хочете обрати - \n[додати учня] \n[увесь журнал]\n[середній бал] - '+
        'середній бал кожного учня' +
        '\n[за середнім] - ' 
        + 'рейтинг учнів за середнім балом'
        + '\n[найвищ] - пошук за найвищим середнім'
        +"\nПотрібна опція: ")

    if choose == 'додати учня':
        user_name = input('Введіть ПІБ учня: ')
        while True:
            marks = list(map(int, input("через пробіл введіть 5 оцінок: ").split()))

            if len(marks) != 5 or max(marks) > 12 or min(marks) < 1:
                print('ТРЕБА РІВНО 5 ОЦІНОК у діапазоні 1-12!')
                continue
            else:
                journal[user_name] = marks
                print('Ви успішно додали учня з оцінками')
                while True:
                    choosing = input("вийти з опції напишіть [так]: ")
                    if choosing == 'так':
                        break
                break

    if choose == 'увесь журнал':
        print(f"УВЕСЬ ЖУРНАЛ - {journal}")
        while True:
            choosing = input("вийти з опції напишіть [так]: ")
            if choosing == 'так':
                break
        continue

    if choose == 'середній бал':
        if len(journal.keys()) < 2:
            print('У вашому журналі немає учнів.Додайте їх, щоб перевірити середній бал')
            while True:
                choosing = input("вийти з опції напишіть [так]: ")
                if choosing == 'так':
                    break
            continue
        while True:
            print(f'\n{journal}\n ')
            pib = input(f"напишіть ПІБ учня, щоб отримати його середнє значення: ").strip()
            if pib not in journal.keys() or pib == 'group_info':
                print('\nнемає такого учня.Спробуйте ще раз')
                continue
            middle = journal[pib]
            print(f'середнє значення - {round(sum(middle) / len(middle))}')
            choosing = None;
            while True:
                choosing = input("вийти з опції напишіть [так]\n"
                +"обрати іншого учня напишіть [ні]\nНапишіть тут: ")

                if choosing == 'так':
                    break

                if choosing == 'ні':
                    break

            if choosing == 'ні':
                continue

            break

    if choose == 'за середнім' or choose == 'найвищ':

        if len(journal.keys()) < 2:
            print('У вашому журналі немає учнів.Додайте їх, щоб перевірити середній бал')
            while True:
                choosing = input("вийти з опції напишіть [так]: ")
                if choosing == 'так':
                    break
            continue
        else:
            arr = []
            for value in journal.values():
                if type(value) == tuple:
                    continue

                average = round(sum(value) / len(value), 2)
                arr.append(average)
            
            index = 1
            arr.sort(reverse=True)

            for i in range(len(arr)):
                name = None
                for key, value in journal.items():
                    if type(value) == tuple:
                        continue
                    average = round(sum(value) / len(value), 2)
                    if average == arr[i]:
                        name = key
                        break
            rate[index] = name
            index += 1
            if choose == 'найвищ':
                print(f'найвищий рейтинг за середнім балом посідає учень - {rate[1]}')
            elif choose == 'за середнім':
                print(f'рейтинг учнів за оцінками - {rate}')

            while True:
                choosing = input("вийти з опції напишіть [так]: ")
                if choosing == 'так':
                     break
    else:
        print('введіть коректну опцію')