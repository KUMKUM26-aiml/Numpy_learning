import numpy as np

a=np.array([23,45,67,10])
b=np.array([[34,5,6,78,2],[45,76,98,10,56]])
print(a)# 1d array
print(b)# 2d array

#shape
print(a.shape)
print(b.shape)

#dimension
print(a.ndim)#1d
print(b.ndim)#2d

#datatype
print(a.dtype)
c=np.array([3.4,5.6,7.8])
print(c.dtype)

#compare list and array
l=[2,3,4,5]
print(l*2)#repeats list
print(a*2)#multiply 2 

d=np.array([1,2,3],dtype=float)#create a array with specific datatype
print(d.dtype)

