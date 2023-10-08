#3 Write a python script to define a class student having members roll no, name, age, gender. Create a subclass called Test with member marks of 3 subjects. Create three objects of the Test class and display all the details of the student with total marks
class Student:
    def __init__(self, roll_no, name, age, gender):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender

class Test(Student):
    def __init__(self, roll_no, name, age, gender, subject1_marks, subject2_marks, subject3_marks):
        super().__init__(roll_no, name, age, gender)
        self.subject1_marks = subject1_marks
        self.subject2_marks = subject2_marks
        self.subject3_marks = subject3_marks

    def calculate_total_marks(self):
        print("Student Details:")
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Total Marks:", self.subject1_marks + self.subject2_marks + self.subject3_marks)
        print()

student1 = Test(1, "John", 18, "Male", 80, 85, 90)
student1.calculate_total_marks()
student2 = Test(2, "Emily", 17, "Female", 75, 82, 88)
student2.calculate_total_marks()
student3 = Test(3, "Michael", 16, "Male", 90, 88, 92)
student3.calculate_total_marks()