from math import *
from random import *
import statistics as stat
import datetime
from student_utils import *
import tkinter
#1

# rad = float(input('Enter radius: '))
# legs_triangle = list(map(float, input('Enter 2 kateti: ').split(', ')))
# stuff = int(input("Enter amount of stuff: "))
# amount = int(input("Enter amount in bag: "))

# def krug(radius = 1):
#     return round(pi * radius ** 2, 2)
# def triangle(first = 0, second = 0):
#     return round(sqrt(pow(first, 2) + pow(second, 2)))
# def amount_in_bag(stuff , amount = 1):
#     return ceil(stuff / amount)

# print(f"\nПлоща круга = {krug(rad)}") 
# print(f"Площа трикутника = {triangle(legs_triangle[0], legs_triangle[1])}") 
# print(f"Потрібно упаковок: {amount_in_bag(stuff, amount)}") 

#2 

# marks = []
# marks_in_range = 0

# for i in range(10):
#     marks.append(randint(1,12))
#     if 10 <= marks[i] <= 12:
#         marks_in_range += 1

# print(f"Оцінки: {marks}")
# print(f"Min: {min(marks)}")
# print(f"Max: {max(marks)}")
# print(f"Середнє: {stat.mean(marks)}")
# print(f"Медіана: {stat.median(marks)}")
# print(f"Оцінок: {marks_in_range}")


#3 
# user_data = list(map(int, input("Дата події(рік-місяць-день): ").split('-')))
# data = datetime.date(user_data[0], user_data[1], user_data[2])
# today_data = datetime.date.today()
# if today_data > data:
#     print(f"{today_data - data} тому була подія")
# if today_data < data:
#     print(f"до події залишилось {data - today_data}")
# if today_data == data:
#     print('0 днів')

#4

students = ["Ivan","Vasya","Petro"]
stud_1, stud_2, stud_3 = {}, {}, {}
def message():
    return int(entry.get()) 

def btn1():
    amount_marks = message()

    stud_1['name'] = students[0]
    stud_2['name'] = students[1]
    stud_3['name'] = students[2]

    stud_1['marks'] = generate_grades(amount_marks)
    stud_2['marks'] = generate_grades(amount_marks)
    stud_3['marks'] = generate_grades(amount_marks)

    stud_1['averange'] = average_grade(stud_1['marks'])
    stud_2['averange'] = average_grade(stud_2['marks'])
    stud_3['averange'] = average_grade(stud_3['marks'])

    stud_1['level'] = get_level(stud_1['averange'])
    stud_2['level'] = get_level(stud_2['averange'])
    stud_3['level'] = get_level(stud_3['averange'])


    lbl_text['text'] = (f"{stud_1['name']}: {stud_1['marks']} | Сер. бал: {stud_1['averange']} | Рівень: {stud_1['level']}\n"
        f"{stud_2['name']}: {stud_2['marks']} | Сер. бал: {stud_2['averange']} | Рівень: {stud_2['level']}\n"
        f"{stud_3['name']}: {stud_3['marks']} | Сер. бал: {stud_3['averange']} | Рівень: {stud_3['level']}"
    )

window = tkinter.Tk()
icon = tkinter.PhotoImage(file="icons/doom-picture.png")
window.iconphoto(False, icon)
window.title('Статистика учнів')
window.geometry('500x400')
label = tkinter.Label(window, text = "Введіть к-сть оцінок від 1 до 20", font =('Arial, 18'))
label.place(x = 0, y = 0)
label.pack()
entry = tkinter.Entry(width = 20)
entry.place(x = 0, y = 40)
entry.pack(ipady=8)
frame = tkinter.Frame(window,pady=10)
frame.pack()
bt1 = tkinter.Button(frame, text = "Сформувати звіт", width = 20, activebackground = "lightgreen", font=("Arial", 14, "bold"), command=btn1)
bt1.grid(row = 0, column = 0, padx = 10)
lbl_text = tkinter.Label(frame, text = "", font = ("Arial, 10"), pady= 20)
lbl_text.grid(row = 1, column = 0, columnspan= 2)
window.mainloop()