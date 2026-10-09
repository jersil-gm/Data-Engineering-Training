# Polymorphism - Example 1
print("*** Polymorphism Example 1 ***\n")
class Developer:
    def work(self):
        print("Developer writes code")
class Tester:
    def work(self):
        print("Tester Tests the application")

d1=Developer()
t1=Tester()
d1.work()
t1.work()

#Polymorphism - Example 2
print("\n*** Polymorphism Example 2 - same method behaving differently (dynamic)***\n")
class Employee:
    def work(self):
        print("Employee Work")
class Developer:
    def work(self):
        print("Developer Work")
class Tester:
    def work(self):
        print("Tester Work")
def perform_work(employee):
    employee.work()
d1=Developer()
t1=Tester()
e1=Employee()
perform_work(d1)
perform_work(t1)
perform_work(e1)