import numpy as np
a=np.arange(100000)
b=list(range(100000))
%time for _ in range(1000):    c=a+5
%time for _ in range(1000):    d=[x+5 for x in b]

import numpy as np
a=np.arange(4)
print("NumPy array is",a)
print("Type of NumPy array is ",type(a))

import numpy as np
l=[1,2,3,4]
print('l is ',l)
print('type(l) is ',type(l))
a=np.array(l)
print('a is ',a)
print('type(a) is ',type(a))

import numpy as np
a=np.random.rand(2,3)
print('a is ',a)
b=np.random.randn(2,3)
print('b is ',b)

import numpy as np
a=np.random.rand(2,3)
print('a is ',a)
print('Number of dimensions of ndarray a are',a.ndim)

import numpy as np
a=np.random.rand(2,3)
print('a is ',a)
print('Dimensions of ndarray a are',a.shape)

import numpy as np
a=np.random.rand(2,3)
print('a is ',a)
print('Data type of ndarray a is',a.dtype)

import numpy as np
a=np.random.rand(2,3)
print('a is ',a)
print('Number of elements in ndarray a is',a.size)



