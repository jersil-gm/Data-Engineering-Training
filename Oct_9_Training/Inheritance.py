# Simple Inheritance
print("\n *** Simple Inheritance - Example 1 ***\n")

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
class Developer(Employee):
    pass
developer=Developer("Karthi",50000)
developer.display()

# Inheritance Example 2
print("\n *** Child Class with a method in it - Inheritance Example 2 ***\n")

class Employee1:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
class Developer(Employee1):
    def write_code(self):
        print("Developer is writing code")
d=Developer("Karthi",50000)
d.display()
d.write_code()