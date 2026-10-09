# Method Overriding
print("*** Method Overriding Example 1 ***\n")
class Employee:
    def work(self):
        print("Employee Work")
class Developer(Employee):
    def work(self):
        print("Developer Work")
e1=Employee()
e1.work()
d1=Developer()
d1.work()