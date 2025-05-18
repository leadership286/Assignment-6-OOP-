class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Create object of the class
student1 = Student("Rimsha Ansari", 98)

# Call the display method
student1.display()
