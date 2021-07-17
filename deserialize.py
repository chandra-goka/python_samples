import pickle

from serialize import Employee

with open("employees.pickle", "rb") as f:
    employees = pickle.load(f)

for employee in employees:
    print(type(employee))
    print(employee.__dict__)