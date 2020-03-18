vowels =['a','e','i','o','u']
elem = input("Enter any statement : ")
data = set(elem)
result = data.intersection(vowels)
print("Vowels present in given statement :",result)