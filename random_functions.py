import numpy as np
#Random numbers 0 to 1
a=np.random.rand(5)
print(a)

#np.random.randint(start, end, size) Random integers
b=np.random.randint(1,50,5)
print(b)

#Random shuffle
arr1=np.array([10,20,30,40,50])
np.random.shuffle(arr1)
print(arr1)

#Random normal distribution
arr2=np.random.randn(5)
print(arr2)