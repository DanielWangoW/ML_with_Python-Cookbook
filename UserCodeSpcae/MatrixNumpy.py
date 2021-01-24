import numpy as np
from scipy import sparse

vector_row = np.array([1, 2, 3])

vector_column = np.array([[1], [2], [3]])

matrix_object = np.mat([[1, 2], [1, 2], [1, 2]])

print(type(vector_row))
print(type(matrix_object))

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matrix_sparse = sparse.csr_matrix(matrix)
add_100 = lambda i: i + 100

vectorized_add_100 = np.vectorize(add_100)

vectorized_add_100(matrix)

vectorized_add_100_sim = matrix + 100

print(matrix)
print(matrix.diagonal())
print(matrix.diagonal(offset=1))
print(vectorized_add_100)
print(vectorized_add_100_sim)

print(matrix.T)

print(matrix.flatten())

print(np.linalg.matrix_rank(matrix))

print(np.linalg.det(matrix))

vector_a = [1, 2, 3]
vector_b = [4, 5, 6]
print(np.dot(vector_a, vector_b))
