import numpy as np

#zeros() and ones() create array of 5 zeroes and 5 ones
zero1=np.zeros(5)
ones1=np.ones(5)

print(zero1)
print(ones1)

#arange
arr1=np.arange(1,11)
print(arr1)

arr2=np.arange(0,20,2)
print(arr2)#(start ,stop,step)

#linsapce equal spacing
arr3=np.linspace(0,10,5)
print(arr3)

#reshape
arr4=np.arange(1,13)
print(arr4)
reshaped=arr4.reshape(3,4)
print(reshaped)

#flatten() and ravel()
arr5=np.array([[1,2,3],[4,5,6]])
print(arr5)
print(arr5.flatten())#convert to 1d again
print(arr5.ravel())#view