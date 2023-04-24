

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

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def PrintGoodMessagge(str):
        return f"this is good {str}"


Jhon_Cena = Employee("Jhon_Cena", 15000, "Instructor")
Richard = Employee("Richard", 25000, "Student")
Anand = Employee.from_dash("Anand-23000-Employee")

print(Anand.PrintGoodMessagge("anand"))
# OR
print(Employee.PrintGoodMessagge("anand"))

# print("Name is =", Anand.name)
# print("Your Total Leaves is =", Anand.no_of_leaves)