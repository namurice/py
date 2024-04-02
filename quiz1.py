import random as rd
import threading
import time

class IsoscelesTrapezoid:
    def __init__(self, sides):
        self.base1 = sides[0]
        self.base2 = sides[1]
        self.height = sides[2]

    def __str__(self):
        return f"bases are {self.base1} and {self.base2} and height {self.height}"

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __add__(self, other):
        return IsoscelesTrapezoid([self.base1 + other.base1, self.base2 + other.base2, self.height + other.height])

    def __mul__(self, other):
        return IsoscelesTrapezoid([self.base1 * other.base1, self.base2 * other.base2, self.height * other.height])
    
class Rectangle(IsoscelesTrapezoid):
    def area(self):
        return self.base1 * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__([side, side, side])

    def area(self):
        return self.base1 ** 2

class Triangle:
    def __init__(self, base_and_height):
        self.base = base_and_height[0]
        self.height = base_and_height[1]

    def area(self):
        return 0.5 * self.base * self.height


def handle_trapezoids():
    trapezoid = IsoscelesTrapezoid([rd.randint(1, 50), rd.randint(1, 50), rd.randint(1, 50)])
    print(trapezoid)

def handle_rectangles():
    rectangles = [Rectangle([rd.randint(1, 50), rd.randint(1, 50), rd.randint(1, 50)]) for _ in range(5)]
    for rectangle in rectangles:
        print(rectangle.area())

def handle_squares():
    square = Square(rd.randint(1, 50))
    print(square.area())

def handle_triangles():
    triangle = Triangle([rd.randint(1, 50), rd.randint(1, 50)])
    print(triangle.area())  

start_time = time.time()

threads = []
threads.append(threading.Thread(target=handle_trapezoids))
threads.append(threading.Thread(target=handle_rectangles))
threads.append(threading.Thread(target=handle_squares))
threads.append(threading.Thread(target=handle_triangles))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Execution time: {time.time() - start_time} seconds")