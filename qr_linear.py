
'''
minimize || Ax - b || using qr factorization
'''

import numpy as np

# create a mxn array, where m > n
A = np.random.rand(10, 3)

b = np.random.rand(10, 1)

# QR decomposition
q,r = np.linalg.qr(A)

# calculate the solution
qtb = np.dot(q.T, b)
x_array = np.linalg.solve(r, qtb)


# print the solution
print x_array


