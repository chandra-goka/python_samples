from collections import OrderedDict

ord_dict = OrderedDict()
ord_dict['A'] = 65
ord_dict['B'] = 66
ord_dict['C'] = 67
ord_dict['D'] = 68

for key, value in ord_dict.items():
    print(f"{key} => {value}")

print("Reverse Order")
for key, value in reversed(ord_dict.items()):
    print(f"{key} => {value}")

data = {"online": 6, "tutorials":9, "point":5}
print("Before Ordered")
print(data)
print("After Ordered")
print(OrderedDict(data))
