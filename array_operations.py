import numpy  as np
#created array arr1 and arr2
arr1=np.array([34,55,67,8])
arr2=np.array([76,89,32,54])

print("array 1: ",arr1)
print("array 2: ",arr2)

#Addition
print("\naddition of arr1 and arr2",arr1+arr2)

#substraction
print("\nsubstration : ",arr1-arr2)

#Multipication
print("\nmultipication: ",arr1*arr2)

#Substarction
print("\nsubstraction: ",arr1/arr2)

#Scalar operations
print("\naddition of 5: ",arr1+5)
print("multipication of 2: ",arr1*2)

#Mathematical functions
print("\nsquare root: ",np.sqrt(arr1))
print("exponetial: ",np.exp(arr1))
print("log: ",np.log(arr1))

#Aggregate functions
print("\nsum: ",np.sum(arr1))
print("mean: ",np.mean(arr1))
print("maximum: ",np.max(arr1))
print("minimum: ",np.min(arr1))

#2d array creation
matrix=np.array([[3,4,5],
                 [7,8,9]])
print(matrix)

print("Row sum: ",np.sum(matrix,axis=1))
print("Column sum: ",np.sum(matrix,axis=0))

