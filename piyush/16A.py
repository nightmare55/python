class Rectangle:
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create a Rectangle object
rectangle1 = Rectangle(5, 4)

# Calculate and print the area and perimeter
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())