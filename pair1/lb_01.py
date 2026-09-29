#ex 1

#a

# number = int(input("enter a number: "))

# if number % 2 == 0:
#     print("number is even")
# else :
#     print("number is odd")

#b

# age = int(input("enter your age: "))

# if age >= 18:
#     print("you are adult")
# else:
#     print("you aren't adult")

#c

# radius = float(input('Enter a radius: '))

# square = radius**2 * 3.14
# Circumference = 2 * 3.14 * radius

# print(square, ' - square',)
# print(Circumference, ' - length of circle')

#d

# a = float(input('enter first number'))
# b = float(input('enter second number'))

# print(max(a,b))


#2

# x, y = map(float, input('введіть координати').split())

# if x == 0 or y == 0:
#     print('ні одна чверть')
# else:
#     if x > 0 and y > 0:
#         print('1 чверть')
#     if x < 0 and y > 0:
#         print('2 чверть')
#     if x < 0 and y < 0:
#         print('3 чверть')
#     if x > 0 and y < 0:
#         print('4 чверть')


#3

# age = int(input('вкажіть вік: '))
# last_num = age % 10
# last_two_nums = age % 100
# if age > 120 or age < 0:
#     print('введіть коректний вік')
# else:
#     if last_num == 1 and last_two_nums != 11:
#         print(age, 'рік')
#     elif last_num < 5 and last_num > 1:
#         if last_two_nums > 11 and last_two_nums < 15:
#             print(age,'років')
#         else:
#             print(age,'роки')

#     else:
#         print(age,'років')

#4

# p1 = 17 #ціна за білет якщо брати поштучно 
# p2 = 120 #ціна за пачку білетів
# k = 10 #к-сть білетів в 1 пачкі
# N = 12 #к-сть поїздок які треба виконати
# result = None
# only_stacks = None

# if k == 1:
#     p1 = p2

# sum = 0
# count_k = 0
# while True:
#     count_k += 1
#     sum += k
#     if sum >= N:
#         break

# only_stacks = count_k * p2

# smaller_portion = N
# cost_k_p1 = None
# if N - k > 0:
#     smaller_portion = N - k
#     cost_k_p1 = (smaller_portion * p1) + p2
# else:
#     cost_k_p1 = p1 * N

# result = min(cost_k_p1, only_stacks)

# print(result)
