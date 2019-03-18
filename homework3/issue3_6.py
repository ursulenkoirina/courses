from math import *
"""
6.1. Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
"""
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

a = is_year_leap(2020)
print(a)

"""
6.2. Функция принимает три числа a, b, c.
Функция должна определить, существует ли треугольник с такими сторонами.
Если треугольник существует, вернёт True, иначе False.
"""

def triangle(a,b,c) :
    if (a + b > c) and (b + c > a) and (c + a > b):
        return True
    else:
        return False

a = triangle(4, 7, 9)
print(a)

"""
6.3 Пишем функцию, которая попросит пользователя ввести слово (строка без пробелов в середине, а вначале и
в конце пробелы могут быть). Пока он не введёт правильно, просите его ввести. Функция возвращает введённое слово
"""
def input_value():
    while True:
        line = input("Input world: ")
        # space = line.strip().count(' ')
        space = ' ' in line.strip()
        if space != 0:
            print("Your line is contain space in the middle", end='\n')
        else:
            print("Your line is ", line, end='\n')
            break
    return line

input_value()
"""
 6.4 Пишем функцию, которая попросит ввести число.
Пока он не введёт правильно, просите его ввести. Функция возвращает введённое число."""
def input_number():
    while True:
        try:
            value = int(input("Input number: "))
            print("Your value is a number", value)
            break
        except ValueError:
            print('Your value is not a number! Try again')
    return value

input_number()
"""
6.5. Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами и если
существует, то возвращает тип треугольника Equilateral triangle (равносторонний), Isosceles triangle (равнобедренный),
Versatile triangle (разносторонний) или не треугольник (Not a triangle).
"""
def triangle_type(a, b, c) :

    if (a + b > c) and (b + c > a) and (c + a > b):
        if a == b == c:
            result = 'Equilateral triangle'
        elif a == b or a == c or b == c:
            result = 'Isosceles triangle'
        else:
            result = 'Versatile triangle'
    else:
        result = "Not a triangle"
    return result

print(triangle_type(5, 5, 5))
"""
6.6 Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющую расстояние
между точкой (x1, y1) и (x2, y2). Считайте четыре действительных числа от пользователя
и выведите результат работы этой функции.
"""

def distance(x1, y1, x2, y2):
    result = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return result

a = distance(5, 7, 3 ,2)
print(a)


