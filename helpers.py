# Module helpers

import numpy as np

from constants import DIMENSION

"""
Create the A matrix of
the linear system of
equations.
"""
def create_matrix_A(gama):
  matrix_A = np.zeros((DIMENSION, DIMENSION), np.double)
  for i in range(DIMENSION):
    for j in range(DIMENSION):
      if i == j:
        matrix_A[i][j] = np.double(gama)
      if (i - 1 == j) or (i == j - 1):
        matrix_A[i][j] = np.double(-1)
  return matrix_A

"""
Create the L matrix as
the bottom left part of
the matrix A.
"""
def create_matrix_L(matrix_A):
  matrix_L = np.zeros((DIMENSION, DIMENSION), np.double)
  for i in range(DIMENSION):
    for j in range(DIMENSION):
      if i > j:
        matrix_L[i][j] = matrix_A[i][j]
  return matrix_L

"""
Create the D matrix as
the diagonal part of
the matrix A.
"""
def create_matrix_D(matrix_A):
  matrix_D = np.zeros((DIMENSION, DIMENSION), np.double)
  for i in range(DIMENSION):
    for j in range(DIMENSION):
      if i == j:
        matrix_D[i][j] = matrix_A[i][j]
  return matrix_D

"""
Create the inverse of
the matrix.
"""
def create_inverse_matrix(matrix):
  return np.linalg.inv(matrix)

"""
Create the b vector of
the right side.
"""
def create_vector_b(gama):
  vector_b = np.full((DIMENSION, 1), gama - 2, np.double)
  vector_b[0] = vector_b[DIMENSION - 1] = np.double(gama - 1)
  return vector_b

"""
Create the x0 start
vector.
"""
def create_vector_x0():
  vector_x0 = np.zeros((DIMENSION, 1), np.double)
  return vector_x0

"""
Check the convergence
of an iterative method.
"""
def check_convergence(matrix):
  eigenvalues, eigenvectors = np.linalg.eig(matrix)
  eigenvalues = [abs(x) for x in eigenvalues]
  return True if (max(eigenvalues) < 1) else False

"""
Stop the calculation
if it meets the stopping
criterion.
"""
def check_stopping_criterion(matrix_A, vector_b, vector_x):
  numerator = calculate_euclidean_norm(matrix_A @ vector_x - vector_b)
  denominator = calculate_euclidean_norm(vector_b)
  bound = np.double(pow(10, -6))
  return True if (numerator / denominator < bound) else False

"""
Calculate the euclidean
norm of the vector.
"""
def calculate_euclidean_norm(vector):
  return np.sqrt(sum(pow(component, 2) for component in vector))

"""
Output the final result
that meets the stopping
criterion.
"""
def output_final_result(results):
  print("(", end = "")
  for i, component in enumerate(results[-1]):
    if i != DIMENSION - 1:
      print(*component, end = ", ")
    else:
      print(*component, end = "")
  print(")\n")

"""
Output all calculated
results including the one
that meets the stopping
criterion.
"""
def output_all_results(results):
  for i, result in enumerate(results):
    print("[" + str(i + 1) + ". ITERATION] (", end = "")
    for j, component in enumerate(result):
      if j != DIMENSION - 1:
        print(*component, end = ", ")
      else:
        print(*component, end = "")
    print(")\n")
