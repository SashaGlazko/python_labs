#1

# N = int(input('enter a number'))
# sum = 0
# amount = 0
# averange = 0

# for i in range(1, N + 1):
#     if i % 5 == 0 or i % 3 == 0:
#         sum += i
#         amount += 1
# if amount > 0 and sum > 0:
#     averange = sum / amount

# print('sum - ',sum,'amount - ', amount, 'averange - ', averange)

#2

# N = int(input('enter a number'))
# if N == 0:
#     print('amount = ', 1, 'sum = ', 0, 'max = ', 0, 'min = ', 0)
# else:
#     min = 9
#     max = 0
#     amount = 0
#     suma = 0

#     while N > 0:
#         digital = N % 10

#         if max < digital:
#             max = digital

#         if min > digital:
#             min = digital
#         amount += 1
#         suma += digital

#         N = N // 10
#     print('amount = ', amount, 'sum = ', suma, 'max = ', max, 'min = ', min)

# 3


# N = int(input("Enter a number: "))

# for i in range(1, N + 1):
#     copy_i = i
#     sum = 0
#     amount = 0

#     while True:
#         digital = copy_i % 10

#         amount += 1

#         if digital == 0:
#             break

#         if i % digital == 0:
#             sum += 1
#         copy_i = copy_i // 10
#         if copy_i == 0:
#             break
#     if sum == amount:
#         print(i)

#4

# width = int(input('Enter width: '))
# height = int(input('Enter height: '))
# border = input('Enter type of border: ')
# content = input('Enter type of content: ')

# if width < 3 or height < 3:
#     print("Enter bigger size of picture")
# else:
#     for h in range(1, height + 1):
#         for w in range(1, width + 1):
#             if h == 1 or h == height :
#                 print(border, end='')
#             else:
#                 if w == 1 or w == width:
#                     print(border, end='')
#                 else:
#                     print(content, end='')
#         print()