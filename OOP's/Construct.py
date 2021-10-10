
class Employee:
    no_of_leaves = 8

    # This is Constructor and self is current object
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


Jhon_Cena = Employee("Jhon_Cena", 15000, "Instructor")

# rohan = Employee()
# Jhon_Cena.name = "Jhon_Cena"
# Jhon_Cena.salary = 15000
# Jhon_Cena.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 25000
# rohan.role = "Student"

print("Your Salary is =",Jhon_Cena.salary)

