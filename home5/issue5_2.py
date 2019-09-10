import math
"""
Создать классы
1) Прямоугольная площадка (пример: комната) (свойства: две стороны).
Методы:
1. вычисляем площадь,
2. вычисляем периметр.
2) Точка на карте (свойства: X, Y).
Методы:
1. Нужно вычислить расстояние до начала координат,
2. * вычисляется расстояние между точкой и другой точкой экземпляром этого же класса
3. ** перевод в другие системы координат
"""


class Room:
    def __init__(self, length=1, width=2):
        self.length = length
        self.width = width

    def square(self):
        result = self.length * self.width
        return result

    def perimeter(self):
        result = (self.length + self.width)*2
        return result


class PointMap:
    def __init__(self, x=-1, y=-2):
        self.x = x
        self.y = y

    def distance_origin(self):
        result = math.sqrt(self.x**2 + self.y**2)
        return result

    def distance_two_point(self, x1=1, y1=1):
        result = math.sqrt((x1 - self.x)**2 + (y1-self.y)**2)
        return result


if __name__ == "__main__":
    p1 = Room(2, 7)
    print(p1.square())
    print(p1.perimeter())
    p2 = PointMap(2, 1)
    print(p2.distance_origin())
    print(p2.distance_two_point())




