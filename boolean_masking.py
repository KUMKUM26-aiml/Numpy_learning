import numpy as np
a=np.array([25,67,4,32])
#comparison operations
print(a>25)
print(a<30)
print(a==25)

#Filtering values
result=a[a>25]
print(result)

#replace using condition
a[a>30]=0
print(a)

#Multiple conditions
b=np.array([10,20,25,34,78,56])
print(b[(b>25) & (b>60)])

matrix=np.array([[10,23,45],
                 [6,89,44]])
print(matrix[matrix>30])

