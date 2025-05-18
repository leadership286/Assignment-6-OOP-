class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f"Employee Name: {self.name}"

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: reference to an existing Employee

    def show_department_info(self):
        return f"Department: {self.dept_name}, {self.employee.get_details()}"

# Create an Employee (independent object)
emp1 = Employee("Rimsha Ansari")

# Create a Department and associate it with the existing Employee
dept1 = Department("IT", emp1)

# Display information
print(dept1.show_department_info())  # Output: Department: IT, Employee Name: Rimsha Ansari
