elem = input("Enter any statement : ")
vowels =['a','e','i','o','u']
list1=[]
for x in elem:
    if (x in vowels and x not in list1):
        list1.append(x)
print("Vowels present in given statement : ",list1)