"""
Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
"""
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

"""
Функция должна определить, существует ли треугольник с такими сторонами.
Если треугольник существует, вернёт True, иначе False.
"""

def triangle(a,b,c) :
    if (a + b > c) and (b + c > a) and (c + a > b):
        return True
    else:
        return False

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

if __name__ == "__main__":
   a = triangle(1,4,6)
   print(a)