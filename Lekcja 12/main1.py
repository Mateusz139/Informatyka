from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159265359 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159265359 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return  self.side **2

    def perimeter(self):
        return 4 * self.side

class Rhombus(Shape):
    def __init__(self, diagonal1, diagonal2, side):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
        self.side1 = side

    def area(self):
        return 0.5 * (self.diagonal1*self.diagonal2)

    def perimeter(self):
        return 4 * self.side1

class Trapezoid(Shape):
    def __init__(self, bottom, top, right, left, height):
        self.bottom = bottom
        self.top = top
        self.right = right
        self.left = left
        self.height = height
    def area(self):
        return 0.5*(self.bottom + self.top)*self.height

    def perimeter(self):
        return self.right + self.left + self.top + self.bottom

if __name__ == '__main__':
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    square = Square(5)
    rhombus = Rhombus(5, 6, 5)
    trapezoid = Trapezoid(5, 6, 5, 5, 5)


    print("Circle Area:", circle.area())
    print("Circle Perimeter:", circle.perimeter())

    print("Rectangle Area:", rectangle.area())
    print("Rectangle Perimeter:", rectangle.perimeter())

    print("Square Area:", square.area())
    print("Square Perimeter:", square.perimeter())

    print("Trapezoid Area:", trapezoid.area())
    print("Trapezoid Perimeter:", trapezoid.perimeter())

    print("Rhombus Area:", rhombus.area())
    print("Rhombus Perimeter:", rhombus.perimeter())









