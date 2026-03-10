import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
#Multipication of matrix
result=np.dot(a,b)
print(result)

#Matrix transpose
c=np.array([[1,2,3],[4,6,8]])
print(c.T)

#Determinant
print(np.linalg.det(a))

#Matrix inverse
print(np.linalg.inv(a))

#Eigenvalues
values,vector=np.linalg.eig(a)
print("Eigen values: ",values)
print("Eigen vectors: ",vector)