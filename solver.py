# Module solver

import helpers as h

from constants import MATRIX_E

def run(method, gama, verbose):
  matrix_A = h.create_matrix_A(gama)
  matrix_L = h.create_matrix_L(matrix_A)
  matrix_D = h.create_matrix_D(matrix_A)
  vector_b = h.create_vector_b(gama)
  vector_x0 = h.create_vector_x0()

  # Set the Q matrix according
  # to the iterative method
  if method == "J":
    matrix_Q = matrix_D
  elif method == "GS":
    matrix_Q = matrix_L + matrix_D

  matrix_Q_inverse = h.create_inverse_matrix(matrix_Q)
  matrix_W = MATRIX_E - matrix_Q_inverse @ matrix_A

  # Check the convergence of
  # the iterative method and
  # calculate all solutions
  if h.check_convergence(matrix_W):
    results = calculate([], matrix_A, matrix_Q, matrix_Q_inverse, vector_b, vector_x0)
    print("Selected iterative method is convergent for this parameter value.")
    print("Solution was found after " + str(len(results)) + " iterations:")
    h.output_all_results(results) if verbose else h.output_final_result(results)  
  else:
    print("Selected iterative method is not convergent for this parameter value.\n")

"""
Solve the linear system
of equations with
the iterative method.
"""
def calculate(results, matrix_A, matrix_Q, matrix_Q_inverse, vector_b, previous_vector_x):
  vector_x = matrix_Q_inverse @ ((matrix_Q - matrix_A) @ previous_vector_x + vector_b)
  results.append(vector_x)

  # Check if the current
  # solution satisfies
  # the stopping criterion
  if h.check_stopping_criterion(matrix_A, vector_b, vector_x):
    return results
  
  return calculate(results, matrix_A, matrix_Q, matrix_Q_inverse, vector_b, vector_x)
