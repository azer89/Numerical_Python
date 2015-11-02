
'''
Backward substitution
'''

import numpy as np

L = np.array([[1.0, 0.0], 
              [1.0, 1.0]])
              
row, col = np.shape(L)
              
b = np.array([1.0, 10.0])

y = b.copy()

for i in range(0, col):   # iterate rows
    for j in range(0, i): # iterate columns
        y[i] = y[i] - L[i][j] * y[j]
        