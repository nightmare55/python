#19 Here is a Python class named Shape and its subclass Square/Circle. The subclass has an __init__ function that takes an argument (Length/Radius). Both classes have methods to calculate the area and volume of a given shape:

class Shape:
    def calculate_area(self):
        return

    def calculate_volume(self):
        return
class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def calculate_area(self):
        return self.length * self.length

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14159 * self.radius * self.radius

s = Square(5)
print("Area of Square:", s.calculate_area())

c = Circle(3)
print("Area of Circle:", c.calculate_area())
