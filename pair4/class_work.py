# колекція - структири даних які дозволяють зберігати у собі набори значень
# list - список(впорядкована змінна колекція)
# grades = [12,3,5,9] 
# numbers = []
# numbers2 = list() # створює пустий список
# print(grades[2]) # зсилання на конкретні елементи
# # print(grades[20]) # помилка
# print(len(grades)) # повертає к-ть елементів у списку
# print(grades[len(grades) - 1]) # повертає останній елемент
# grades[2] = 6 # перезапише значення
# print(grades)


# numbers.append(5)
# numbers.append(6)
# numbers.insert(1,2) # за індексом 1 додає число 2.ВІН НЕ ЗАМІНЮЄ ЗНАЧЕННЯ!
# numbers.insert(10,2) # за індексом останнім(не 10) додає число 2.ВІН НЕ ЗАМІНЮЄ ЗНАЧЕННЯ!
# numbers.extend([3,4,5,6,'7']) # додавання кількох елементів в кінець обов'язково описувати це в []
# numbers.remove(5) # видалити перше найдене значення 5. Інакше(якщо не знайдено) то помилка

# if "6" in numbers:
#     numbers.remove("6")

# numbers.pop(-1) # видаляє елемент за індексом

# del numbers[1] # можна видалити за індексом аналогічно
# del numbers # але використовується del білььше для видалення списків

# numbers.clear() # очистити список

# print(numbers.count(5)) # к-сть шуканих елементів
# print(numbers.index(6)) # знайти індекс шуканого елемента
# print(20 in numbers) # чи існує 20 в масиві(True чи False)


# len() довжина 
# print(min('a', 'b', 'c')) - 'a'
# max()
# sum() -знайти суму
# if len(numbers) > 0:
#     average = sum(numbers) / len(numbers) середнє значення
# print(numbers.sort()) у порядку зростання елементи масиву виставляє
# print(numbers.sort(reverse = True)) у порядку спадання
# sort() - він змінює масив і треба його перезаписати, і відразу в print(numbers.sort()) - неможна!
# print(sorted(numbers)) sort але не змінює масив
# numbers.reverse() перевертає масив
# print(numbers[1:3]) - зріз
# print(numbers[::-1]) - перевернути як і reverse
# print(numbers[::2]) - через 1 записати масив

# for number in numbers:
#     print(number) перебрати елементи списку
# print(numbers)

# digits = [-1, 0, 4, -5, 3, -6]
# dodatni = []
# parni = []

# for digit in digits:
#     if digit % 2 == 0:
#         parni.append(digit)
#     if digit > 0:
#         dodatni.append(digit)
# print(dodatni)



# tuple - кортеж(впорядкована незмінна колекція(константний масив))
# rgb = (255, 0, 0)
# r,g,b = rgb # можна розпаковувати кортежі в змінні
# print(r, g, b) 

# data = ()
# a = (1,) # при type(a) це буде просто змінна. якщо додати кому, то це буде саме кортеж
# # rgb[1] = 255 # індексація така сама як і в масивах

# point = (4, -6)
# point = point + (4,) # можна додати в кінець кортежу елемент(тут ми його перезаписали з додатковим елементом в кінці)
# print(point)
# a = (30, 40)
# b = (50, 60)
# c = a + b
# d = a[:1] + b[::] # можна видалити у новому кортежі елемент за допомогою зрізу
# print(c)

# c.count()
# c.index() працюють кортежами
# len(c)

# # set - множина(послідовність унікальних елементів) унікальні - без повторів
subjects = {"Python", "HTML","CSS","Javascript", "Python"}
print(subjects) # другий Python не виведеться(повтори прибираються)
data = {}
print(type(data)) # dict буде(а не множина)
data2 = set() # створити пусту множину
data2.add("Python") # додати один елемент(додавати Python як повторюваний елемент не можна)
data2.update(["CSS", "HTML"]) # додати декілька елемент
data2.remove("HTML") # видалити елемнт(але якщо такого не буде, то буде помилка)
data2.discard("C++") # видалити елемнт(але якщо такого не буде, то не буде помилки)
deleted = data2.pop() # видалить один елемент в кінці, бо в множинах немає індексів
#clear() -також працює в множинах

# if "Python" in data2:
#     print("Python")
# print(data2)


# print(data2)


# names = ["Ivan", "Ivan", "Olha","Vadym"]
# new_names = set(names)
# print(new_names) # видалити всі повторення в масиві

# names1 = {"Ivan","Ivan","Irina"}
# names2 = {"Olha","Vadym", "Ivan"}
# names3 = names1 | names2 # додати множини і записати в змінну
# names4 = names1 & names2 # перетин 2 множин {"Ivan"}
# names5 = names1 - names2 # віднімання двох множин(віднімаємо спільні значення)
# names6 = names2 - names1 # {"Vadym", "Irina"}
# print(names3)

# # dict - словники(пари з ключа та значення)
# student = {
#     "name": "Ivan",
#     "age": 18
# }
# products = ['bread', "milk", "apple", "banaba"]
# prices = [30, 50, 50, 80]

price = {
    'apple':50,
    'apple':40,
    'banana':70,
    'milk':50,
    'bread':30,

}

# students = {} створити пустий об'єкт
# students2 = dict()

price['tea'] = 75
price['bread'] = 35 # можна перезаписувати значення
price.update(
    {
        "juice": 50,
        "coffee": 70
    }
)
# deleted = price.pop('milk') # видалення значень в об'єкті
# del price['milk']

# переглянути роботу методів
# .get()
# .value()
# .key()
# .items()

for key, value in price.items():
    print(key)
    print(value)

print(price)
