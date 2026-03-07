import numpy as np

arr1=np.array([10,20,30])
#scalar broadcasting
print(arr1+5)

arr2=np.array([3,4,9])
#array+array
print("Addition: ")
print(arr1+arr2)

#2D broadcasting
matrix=np.array([[23,5,6],
                 [7,8,9]])

vector=np.array=([5,1,2])
print("Broadcasting: ")
print(matrix+vector)

#column broadcasting
column = np.array([[10],
                   [20]])
print("column Broadcasting: ")
print(matrix+column)