#4 Define a class Employee having members id, name, department, salary. Create a subclass called manager with member bonus. Define methods accept and display in both the classes. Create n objects of the manager class and display the details of the manager having the maximum total salary (salary+bonus)
class Employee:
    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    def accept(self):
        self.id = int(input("Enter employee id: "))
        self.name = input("Enter employee name: ")
        self.department = input("Enter employee department: ")
        self.salary = float(input("Enter employee salary: "))

    def display(self):
        print("Employee ID:", self.id)
        print("Employee Name:", self.name)
        print("Employee Department:", self.department)
        print("Employee Salary:", self.salary)

class Manager(Employee):
    def __init__(self, id, name, department, salary, bonus):
        super().__init__(id, name, department, salary)
        self.bonus = bonus

    def accept(self):
        super().accept()
        self.bonus = float(input("Enter manager bonus: "))

    def display(self):
        super().display()
        print("Manager Bonus:", self.bonus)
n = int(input("Enter the number of managers: "))
managers = []
for i in range(n):
    manager = Manager(None, None, None, None, None)
    manager.accept()
    managers.append(manager)
max_salary_manager = max(managers, key=lambda m: m.salary + m.bonus)
print("\nDetails of the manager with maximum total salary (salary + bonus):")
max_salary_manager.display()