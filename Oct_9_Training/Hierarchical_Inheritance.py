# Hierarchical Inheritance
print("\n *** Hierarchical Inheritance - One Parent class - Multiple child Class ***\n")

class Employee:
    def work(self):
        print("Employee Work")

class Developer(Employee):
    def code(self):
        print("Developer Writes code")
class Tester(Employee):
    def test(self):
        print("Testing Application")
print("** Accessing Parent class Method using the child class - Tester ***\n")
t=Tester()
t.work()
t.test()
print("\n** Accessing Parent class Method using the child class - Developer ***\n")
d=Developer()
d.work()
d.code()
print()
e=Employee()
e.work()
