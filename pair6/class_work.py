# import math підключити бібліотеку встроєну в пайтон
# import math
from math import * # від бібліотеки підключити все.Завантажую в проєкт.Типу скачав
# до назви бібліотеки можна не звертатись
import statistics as stat
import random
from datetime import date # підключити всю бібліотеку, але з неї конкретно якусь функцію
import demo # підключили свою бібліотеку
from tkinter import *

# import statistics as stat даємо псевдонім бібліотеці. Звертатись за stat.inf(...) а не statistic.inf(...)

# a = [10,15,50,20,30]

# # print(f"Середній бал: {stat.mean(a)}")
# r = int(input('f = '))
# circle_area =  round( pi * pow(r, 2), 2)
# print(circle_area)

# balls = 25
# n = 6

# print (f" Повністю заповнених коробок {floor(balls / n)}")
# print (f" Всього коробок {ceil(balls / n)}")

# numbers = []

# for i in range(10):
#     numbers.append(random.randint(1, 100))
# print(f" випадкові 10 чисел {numbers}")

# selected = random.choice(numbers)
# print(f" випадкове із послідовності {selected}")

# print(f'today is {date.today()}')
def text():
    lbl_text['text'] = "hello world"


def clear(event):
    lbl_text['text'] = ""



window = Tk()
window.title('привіт') # створити заголовок
window.geometry('500x400') # розміри за замовчуванням
window.resizable(False, False) # заборонити зміну по висоті та ширині
window["bg"] = "#F19CBB"
label = Label(window, text = "Супер-пупер гламурна програма", font =('Arial, 18'), bg = '#F19CBB', pady = 20)
label.place(x = 0, y = 0)
label.pack()
frame = Frame(window, bg = "#F19CBB")
frame.pack()
bt1 = Button(frame, text = "OK", width = 7, activebackground = "lightgreen", command = text)
bt1.grid(row = 0, column = 0, padx = 10)
bt2 = Button(frame, text = "Cancel", width = 7, activebackground = "lightgreen")
bt2.grid(row = 0, column = 1, padx = 10)
bt2.bind("<Button-1>", clear)
lbl_text = Label(frame, text = "", font = ("Arial, 18"), bg = "#F19CBB", pady= 20)
lbl_text.grid(row = 1, column = 0, columnspan= 2)


window.mainloop()