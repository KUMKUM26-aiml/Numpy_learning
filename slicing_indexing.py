import numpy as np

#create a 1d array
arr1=np.array([10,20,45,67,89])
print(arr1)

#Access element
print("first element ",arr1[0])
print('last element ',arr1[-1])

#slicing 
print("first three elemet ",arr1[0:3])
print("elements from index 2 ",arr1[2:])
print("elements till index 3 ",arr1[:3])
print("every second element ",arr1[::2])

#create 2d array
arr2=np.array([[34,56,78,90],
               [4,5,6,7],
               [12,44,32,42]])
print(arr2)

#access specific element
print("elemet at row 1 column 2: ",arr2[1,2])

#access row
print("row element: ",arr2[0])
#access column
print("column element: ",arr2[:,0])

#slice sub mattix
print("top left 2x2 matrix ")
print(arr2[0:2,0:2])

