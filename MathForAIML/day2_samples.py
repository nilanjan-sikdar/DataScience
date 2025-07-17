import numpy as np

# Advanced Linear Algebra

# Determinant of an array
A = np.array([[2, 3], [1, 4]])
determinant = np.linalg.det(A)
# print("Determinant of A:", determinant)

# Inverse of a matrix
B = np.array([[1, 2], [3, 4]])
inverse = np.linalg.inv(B)
# print("Inverse of A:\n", inverse)

# Eigenvalues and eigenvectors
eigenValue, eigenVector = np.linalg.eig(A)
# print("Eigenvalues of A:", eigenValue)
# print("Eigenvectors of A:\n", eigenVector)

# SVD(1st time learn) ---> Singular Value Decomposition ---> A = U * S * V.Transpose 
# where S is a diagonal matrix of singular values U andf V left and right orthogonal vector


U, S, V = np.linalg.svd(A)
# print("U:\n", U)
# print("S:\n", S)
# print("V:\n", V)

# Reconstract
Sigma = np.zeros((2,2))
np.fill_diagonal(Sigma, S)
Reconstructed = U @ Sigma @ V.T
print("Reconstracted:\n", Reconstructed)
# Hands on Exercises

# ex 1
D = np.array([[2,4],[4,5]])
D_determinant = np.linalg.det(D)
# print("Determinant of D:", D_determinant)

D_inverse = np.linalg.inv(D)
# print("Inverse of D:\n", D_inverse)
# 
# ex 2
eigenVal, eigenVec =np.linalg.eig(D)
# print("Eigenvalues of D:", eigenVal)
# print("Eigenvectors of D:\n", eigenVec)
# 
# ex 3
u, s, v = np.linalg.svd(D)
# print("U:\n", u)
# print("S:\n", s)
# print("V:\n", v)

