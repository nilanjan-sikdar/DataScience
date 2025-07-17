import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# print("Addition: \n", A + B)
# print("Subtraction: \n", B - A)

C = 2 * A
# print("Scalar Multiplication \n", C)

result = np.dot(A, B)

# print("Matrix Multiplication \n", result)

I = np.eye(5)
# print("Identity Matrix \n", I)

Z = np.zeros((2, 3))
# print("Zero Matrix \n", Z)

D = np.diag([1, 2, 3])
print("Diagonal Matrix\n", D)

# ex 1
# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[9, 8], [7, 6]])

# Addition
print("Addition\n", A + B)

# Subtraction
print("Subtraction\n", A - B)

# Scalar Multiplication
print("Scalar Mult: \n", 3 * A)

# ex 2
# Create matrix and vector
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = np.array([1, 0, -1])

# Matrix-vector multiplication 
result = np.dot(M, v)
print("Matrix-Vector Multiplication: \n", result)

# ex 3
# Identity Matrix
I = np.eye(3)
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("A X I:\n", np.dot(A, I))

# Diagboal and Zero Matrix
D = np.diag([1, 7, 9])
Z = np.zeros((3, 3))
print("Diagonal Matrix\n", D)
print("Zero Matrix\n", Z)