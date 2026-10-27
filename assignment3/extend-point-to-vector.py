# J-D Laurence

# Task 5

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def distance_from(self, other):
        #return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return math.dist((self.x, self.y), (other.x, other.y))


class Vector(Point):
    # we are not adding new behaviour in the init so can skip this
    #def __init__(self, x, y):
    #    super().__init__(x, y)

    def __str__(self):
        return f"[{self.x},{self.y}]"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented


# testing
if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    print("--- Point ---")
    print(f"p1 = {p1}, p2 = {p2}")
    print(f"p1 == Point(1, 2): {p1 == Point(1, 2)}")
    print(f"p1 == p2: {p1 == p2}")
    print(f"Distance from p1 to p2: {p1.distance_from(p2)}")

    print("\n--- Vector ---")
    print(f"v1 = {v1}, v2 = {v2}")
    v3 = v1 + v2
    print(f"v1 + v2 = {v3}")
    print(f"Result is a {type(v3).__name__}")