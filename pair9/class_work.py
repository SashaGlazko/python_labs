# book_dict = {
#     "title": 'Кобзар',
#     "author": 'Тарас Шевченко',
#     'copies': 15,
# }

# print(book_dict['title'])

# class Book:
#     def __init__(self, title, price, copies): # для запуску нашого класу використовується __init__ в нього має бути 1 параметр self - (стандарт)
#         self.title = title
#         self.price = price
#         self.copies = copies
#     def avaliable(self):
#         return self.copies > 0
# book1 = Book("Кобзар", 450, 15)
# book2 = Book("Лісова пісня", 200, 0)

# print("first - ",book1.title, book2.price)
# print("second - ",book1.title, book2.price, book2.avaliable())

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def area(self):
        return self.width * self.height
    def info(self):
        print(f"Розміри прямокутника {self.width} X {self.height}")
        print(f"S = {self.area()}")
        print(f"P = {self.perimeter()}")

a = int(input('Enter width: '))
b = int(input('Enter height: '))

rectangle = Rectangle(a, b)