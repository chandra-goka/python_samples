#Solution 1
elem = eval(input("Enter List of values : "))
list1=[]
for x in elem:
    if x not in list1:
        list1.append(x)
print("After Removing duplicate elements ",list1)

#Solution 2
list1=[10,20,30,10,50,20,10,60,80,50,40,10]

newlist=[ele for n,ele in enumerate(list1) if ele not in list1[:n]]

print("New List : ",newlist)

#Solution 3
list1 = ['a','c','a','d','e','a','f','b']  
list2 = sorted(set(list1),key=list1.index)  
print(list2)

#Solution 4
elem = eval(input("Enter List of values : "))
set1 = set(elem)
print("After Removing duplicate elements ",set1)

#Solution 5
list1 = ["abc", "xyz", "pqr"]
list2 = ["aei", "oup", "xyz","abc"]

newSet= set(list1).symmetric_difference(list2).union(set(list1).intersection(list2))

print(newSet)