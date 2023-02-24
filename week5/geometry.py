from math import sqrt 
from functools import reduce
from operator import add

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    
class Geometry:
    
    @staticmethod
    def distance(p1: Point, p2: Point):
        return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
    
    @staticmethod
    def middle(p1: Point, p2: Point):
        mid_x = (p1.x + p2.x)/2
        mid_y = (p1.y + p2.y)/2
        return Point(mid_x, mid_y)
    
    @classmethod
    def perimeter(cls, list_of_points: list):
        return reduce(add, [cls.distance(list_of_points[i], list_of_points[(i+1)%len(list_of_points)]) for i in range(len(list_of_points))], 0)

    @classmethod
    def is_triangle_isoscel(cls, p1: Point, p2: Point, p3: Point):
        side1 = cls.distance(p1, p2)
        side2 = cls.distance(p2, p3)
        side3 = cls.distance(p3, p1)
        if any([side1 == side2, side2 == side3, side3 == side1]):
        # if side1 == side2 or side2 == side3 or side3 == side1:
            return True
        return False