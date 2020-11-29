import numpy as np

# Array Multiplication
arr1 = np.array([[1,2,3],[1,2,3]])
arr2 = np.array([[4,5,6],[4,5,6]])

print(arr1*arr2)

# Matrix Multiplication

arr1=np.arange(0,9).reshape(3,3)
print("First matrix is:")
print(arr1)
arr2=np.arange(1,10).reshape(3,3)
print("second matrix is:")
print(arr2)

arr3=np.dot(arr1,arr2)
print("matrix product of arr1 and arr2 is:")
print(arr3)

arr4=arr1.dot(arr2)
print("Output : ", arr4)

