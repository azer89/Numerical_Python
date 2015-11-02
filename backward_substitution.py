
'''
Backward substitution
'''

import numpy as np

L = np.array([[3.0, 1.0, 1.0], 
              [0.0, 2.0, 1.0],
              [0.0, 0.0, 2.0]])
              
row, col = np.shape(L)

b = np.array([3.0, 2.0, 1.0])

y = b.copy()

# last row
y[col - 1] = y[col - 1] / L[col - 1][col - 1]

for i in range(col - 2, -1, -1):
    for j in range(col - 1, i, -1):
        print y[i], "- ", L[i][j], " * ", y[j]
        y[i] = y[i] - L[i][j] * y[j]
    y[i] = y[i] / L[i][i]