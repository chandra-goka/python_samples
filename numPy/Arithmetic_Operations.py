import numpy as np
A= np.arange(1,11)
print("Array A is:")
print(A)
C=A+4
print("Array C is:")
print(C)

D=A-2
print("Array D is:")
print(D)
E=A/2
print("Array E is:")
print(E)
F=A*2
print("Array F is:")
print(F)

B=np.sqrt(A)
print("Array B is :")
print(B)


C=np.log(A)
print("Array C is :")
print(C)

D=np.sin(A)
print("Array D is :")
print(D)

E=np.cos(A)
print("Array E is :")
print(E)

F=np.tan(A)
print("Array F is :")
print(F)

b= A.sum()
print("sum of elements of array A is:")
print(b)

min=A.min()
print("Minimum number among the elements of A is:")
print(min)

max=A.max()
print("Maximum number among the elements of A is:")
print(max)

e= A.mean()
print("Average of elements of array A is:")
print(e)


