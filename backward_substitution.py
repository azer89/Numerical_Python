
'''
Backward substitution
'''

import numpy as np

# In[]
'''
Function to perform backward substitution
'''
def backsub(U, b):
    row, col = np.shape(U)
    y = b.copy()

    # last row
    y[col - 1] = y[col - 1] / U[col - 1][col - 1]
    
    for i in range(col - 2, -1, -1):
        for j in range(col - 1, i, -1):
            y[i] = y[i] - U[i][j] * y[j]
        y[i] = y[i] / U[i][i]
    
    return y
    
# In[]
    
U = np.array([[3.0, 1.0, 1.0], 
              [0.0, 2.0, 1.0],
              [0.0, 0.0, 2.0]])

b = np.array([3.0, 2.0, 1.0])

y = backsub(U, b)



