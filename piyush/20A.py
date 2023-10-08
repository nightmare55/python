#20 Write a python program to create a class Circle and Compute the Area and the circumferences of the circle.(use parameterized constructor) 

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def compute_area(self):
        return 3.14159 * self.radius * self.radius
    
    def compute_circumference(self):
        return 2 * 3.14159 * self.radius

radius = float(input("Enter the radius of the circle: "))
c = Circle(radius)
print("Area of the circle:", c.compute_area())
print("Circumference of the circle:", c.compute_circumference())