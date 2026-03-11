import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

#vertical stack
result=np.vstack((arr1,arr2))
print(result)

#Horizontal stack 
result2=np.hstack((arr1,arr2))
print(result2)

#Column stack
result3 =np.column_stack((arr1,arr2))
print(result3)

#split array 
a=np.array([1,2,3,4,5,6])
result4=np.split(a,3)
print(result4)

#split 2d array
matrix=np.array([[1,2],
                 [3,4],
                 [4,5],
                 [7,8]])
result5=np.vsplit(matrix,2)