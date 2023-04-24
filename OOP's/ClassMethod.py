

class Employee:
    no_of_leaves = 8

    # This is Constructor and self is current object
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_learves(cls, newLeaves):
        cls.no_of_leaves = newLeaves


Jhon_Cena = Employee("Jhon_Cena", 15000, "Instructor")
Richard = Employee("Richard", 25000, "Student")

Jhon_Cena.change_learves(25)

print(Jhon_Cena.no_of_leaves)
