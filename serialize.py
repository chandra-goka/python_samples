import pickle
from datetime import date


class Employee:
    def __init__(self, name: str, joining_date: str, designation: str) -> None:
        self.name = name
        self.joining_date = joining_date
        self.designation = designation


emp1 = Employee("Chandra Shekhar", date(2020, 2, 6), "SDE")
emp2 = Employee("John", date.today(), "RM")
emp3 = Employee("Peter", date(2019, 12, 16), "Architect")

employees = [emp1, emp2, emp3]

with open("employees.pickle", "wb") as f:
    pickle.dump(employees, f)