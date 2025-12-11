#task 5
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Point: {self.x}, {self.y}"
    
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 )
    
class Vector(Point):
    def __str__(self):
       return f"Vector: {self.x}, {self.y}"
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


#class Point
p1 = Point(3, 4)
p2 = Point(4, 5)
print(p1)
print(p2)
print(p1 == Point(3,4))
print(p1.distance(p2))

#class Vector
v1 = Vector(3, 4)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)