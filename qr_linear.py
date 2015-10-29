
'''
minimize || Ax - b || using qr factorization
'''

import numpy as np

# create a mn x n array, where m >= n
A = np.random.rand(10, 5)

b = np.random.rand(10, 1)

# QR decomposition
q,r = np.linalg.qr(A)

# calculate the solution
qtb = np.dot(q.T, b)
x_array = np.linalg.solve(r, qtb)

# if m = n, C is an identity matrix
C = np.dot(q, q.T)

# print the solution
print x_array


