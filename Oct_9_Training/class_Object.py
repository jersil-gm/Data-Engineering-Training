print("\n **** Class and Object ****\n")
class Employee:
    _department="IT"
class Product1:
    name="Headphones"
    price=290000

p=Product1()
print(p.name,p.price)

# Dynamic class creation and method creation and self usage
print()
print("**** Dynamic class creation and method creation and self usage\n")
class Product:
    name=""
    price=0
    quantity=0
    def total_price(self):
        return self.price*self.quantity

    def display(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")

p1=Product()
p1.name="Laptop"
p1.price=50000
p1.quantity=2
print(f"Total Price of {p1.quantity} {p1.name} : {p1.total_price()}")
p1.display()

p2=Product()
p2.name="Mouse"
p2.price=2000
p2.quantity=3
print(f"Total Price of {p2.quantity} {p2.name} : {p2.total_price()}")
p2.display()

# Protected and Public Variable
print()
print("**** Protected and Public Variables ****\n")
class Employee1:
    _department="IT" # Protected variable
e=Employee1()
print(e._department)

class Employee2:
    __bonus=1000 # private variable
e1=Employee2()
#print(e1.__bonus) # will throw error

# Constructor creation
print("\n *** Constructor ****\n")
class Product:
    def __init__(self):
        print("Product Constructor")
p1=Product()
print()

class Employee3:
    def __init__(self,emp_id,name,dept,salary):
        self.emp_id=emp_id
        self.name=name
        self.dept=dept
        self.salary=salary
    def display(self):
        print(f"Emp_id: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.dept}")
        print(f"Salary: {self.salary}")

e2=Employee3(101,"Aman","IT",80000)
e3=Employee3(102,"Sam","HR",50000)
e3.display()
e2.display()



