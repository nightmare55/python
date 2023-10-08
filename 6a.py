# 6 Write a Python script using the package to calculate the area and volume of a cube and a sphere.
import math

def cube_area(side_length):
    return 6 * side_length ** 2

def cube_volume(side_length):
    return side_length ** 3

def sphere_area(radius):
    return 4 * math.pi * radius ** 2

def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

cube_side_length = float(input("Enter the side length of the cube: "))
sphere_radius = float(input("Enter the radius of the sphere: "))

print("Cube:")
print("Area:", cube_area(cube_side_length))
print("Volume:", cube_volume(cube_side_length))

print("Sphere:")
print("Area:", sphere_area(sphere_radius))
print("Volume:", sphere_volume(sphere_radius))