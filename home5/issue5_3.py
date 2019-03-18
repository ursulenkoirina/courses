"""
Задание 3 (на создание тестов c помощью unittest)

Создайте наборы тестов на написанные функции из прошлого домашнего задания:
Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами.
Если треугольник существует, вернёт True, иначе False.
Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник
с такими сторонами и если существует, то возвращает тип треугольника Equilateral triangle (равносторонний),
Isosceles triangle (равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not a triangle).
"""
import unittest
from home5.last_home import *


class Test(unittest.TestCase):

    def test_year_leap(self):
        result = is_year_leap(2020)
        # self.assertFalse(result)
        self.assertTrue(result)

    def test_year_leap(self):
        result = is_year_leap(1991)
        self.assertFalse(result)

    def test_triangle_test(self):
        result = triangle(4, 7, 9)
        self.assertTrue(result)

    def test_triangle_test(self):
        result = triangle(1, 4, 6)
        self.assertFalse(result)

    def test_triangle_type_test(self):
        result = triangle_type(5, 5, 5)
        self.assertEqual(result, 'Equilateral triangle')

    def test_triangle_type_test(self):
        result = triangle_type(1, 3, 1)
        self.assertEqual(result, 'Not a triangle')

    def test_triangle_type_test(self):
        result = triangle_type(1, 3, 1)
        self.assertNotEquals(result, 'Equilateral triangle')

if __name__ == "__main__":
    unittest.main()