class Person:
    def _init_(self, name, address):
        self.name = name
        self.address = address

class Employee(Person):
    def _init_(self, name, address, staff_salary):
        super()._init_(name, address)
        self.staff_salary = staff_salary

# Create 'n' objects of the Employee class
n = int(input("Enter the number of employees: "))
employees = []

for i in range(n):
    name = input("Enter name of employee {}:".format(i + 1))
    address = input("Enter address of employee {}:".format(i + 1))
    salary = float(input("Enter staff salary of employee {}:".format(i + 1)))

    employee = Employee(name, address, salary)
    employees.append(employee)

# Display details of all employees
print("\nEmployee Details:")
for i, employee in enumerate(employees):
    print("Employee {}: Name - {}, Address - {}, Salary - {}".format(i + 1, employee.name, employee.address, employee.staff_salary))