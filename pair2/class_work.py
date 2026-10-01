# print(1)
# print(2)
# print(3) не зручно
# print(4)
# print(5) 

# i - ітерація.Одне виконанння циклу. I [0,4]. (0,5),step можемо додавати
# for i in range(5):
#     i = i + 1 #i += 1 - інкремент(збільшення на 1). i -= 1(декремент)
#     print(i)

# for i in range(1,6):
#     print(i)

# for i in range(1, 11, 2): #step. Яку інерацію пропускаємо
#     print(i)

# for i in range(10, 0, -1): #можемо і від'ємні цикли
#     print(i)

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# suma = 0

# n = int(input()) # 10

# for i in range(1, n + 1):
#     suma += i
# print(suma)

# f = 1

# n = int(input())

# for i in range(1, n + 1):
#     f *= i
# print(f)

# n = int(input())
# count = 0
# for i in range(1,n + 1):
#     if i % 2 == 0:
#         count += 1
# print(count)


# game = True
# while game:
#     n = int(input('Enter number, for exit Enter - 0: '))
#     if n == 0:
#         game = False


# while True:
#     n = int(input('Enter number, for exit Enter - 0: '))

#     if n == 0:
#         break

# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i)

# n = 62561354
# suma = 0

# while n > 0:
#     digit = n % 10
#     suma += digit
#     n = n // 10
# print(suma)

# maximum = 0
# n = 1231944

# while n > 0:
#     digit =  n % 10
#     if maximum < digit:
#         maximum = digit
#     n = n // 10
# print(maximum)

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i,j)

# width = 8
# height = 4

# for i in range(height):
#     for j in range(width):
#        print('*', end=('')) 
#     print()
