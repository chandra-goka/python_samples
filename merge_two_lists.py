#Merge using + operator
list1 = [10, 20, 30]
list2 = [40, 50, 60]
merged_list = list1+list2

print("Merged List: ",merged_list)

#It is also equivalent to above code using +=

list1 += list2
print("Merged List using +=: ",list1)

#Merge using PEP
list1 = [10, 20, 30]
list2 = [40, 50, 60]

mergedList = [*list1, *list2]
print(mergedList)

#Merge using chain
import itertools

list1 = [10, 20, 30]
list2 = [40, 50, 60]

for item in itertools.chain(list1, list2):
    print(item)

#Merge using list and set
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

merged_list = list(set(list1+list2))
print("Merged List with out duplicates: ",merged_list)

#Merge using list and set
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

list1.extend(list2)
print(list1)

