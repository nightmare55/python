#15 Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributes.
class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

s = Student("sahil", 80)

print("Original Name:", s.student_name)
print("Original Marks:", s.marks)

s.student_name = "piyush"
s.marks = 90

print("Modified Name:", s.student_name)
print("Modified Marks:", s.marks)
