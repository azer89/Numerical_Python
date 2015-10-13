# solve linear equations Ax = b

import numpy as np

# matrix A
a = np.array([[3, 1, 1], 
              [1, 2, 0],
              [1, 2, 1]])

# vector b            
b = np.array([9, 8, 1])

# solve the linear system of equations
x = np.linalg.solve(a, b)

# print result
print x