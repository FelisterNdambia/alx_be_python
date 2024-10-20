import math

# Base class - Shape
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")


# Derived class - Rectangle (inherits from Shape)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # Area of rectangle = length * width


# Derived class - Circle (inherits from Shape)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)  # Area of circle = π * r²
