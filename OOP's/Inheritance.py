

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

class Programmers(Employee):
    def __init__(self, aname, asalary, arole, alanguages):
        # Super is use for doing this
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = alanguages 

    def showMessage(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}. The languags are {self.languages}"

Jhon_Cena = Employee("Jhon_Cena", 15000, "Instructor")
Anand = Employee.from_dash("Anand-23000-Employee")

Ram = Programmers("Ram", 1500, "Programmer", ['C','CPP'])
Sham = Programmers("Sham", 150, "Web Programmer", ['Python'])

print(Ram.showMessage())