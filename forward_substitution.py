
'''
Forward substitution
'''

import numpy as np

# In[]

def forwardsub(L, b):
    y = b.copy()

    # first row
    y[0] = y[0] / L[0][0]
    
    for i in range(1, col):   # iterate rows
        for j in range(0, i): # iterate columns
            y[i] = y[i] - L[i][j] * y[j]
        y[i] = y[i] / L[i][i]
    
    return y
    
# In[]

L = np.array([[2.0, 0.0], 
              [1.0, 2.0]])
              
row, col = np.shape(L)
              
b = np.array([1.0, 10.0])

y = forwardsub(L, b)


    
