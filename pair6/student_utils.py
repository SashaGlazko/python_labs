from random import *
import statistics as stat

def generate_grades(count):
    amount = []
    for i in range(count):
        amount.append(randint(1,12))
    return amount

def average_grade(grades):
    return stat.mean(grades)

def get_level(average):
    if 10 <= average <= 12:
        return 'Високий'
    if 7 <= average < 10:
        return 'Достатній'
    if 4 <= average < 7:
        return 'Середній'
    return 'Низький'