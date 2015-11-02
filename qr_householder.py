
'''
QR Decomposition using Householder reflection
'''

import numpy as np

M = 15 # row
N = 5  # column
A = np.random.rand(M,N)
R = A.copy()

for k in range(0, N):
    x = R[k:M,k].copy()
    e = np.zeros(len(x))
    e[0] = 1.0
    u = -cmp(x[0], 0) * np.linalg.norm(x, 2) * e - x
    u = u / np.linalg.norm(u, 2)
    u_t = u.reshape((1, len(u))) 
    
    u = u.reshape(len(u), 1)
    I = np.eye(len(u), len(u))
    F = I - 2.0 * np.dot(u, u_t) 
    Q_k = np.eye(M, M)
    
    for j in range(k, N):        
        utA = np.dot(u.T, R[k:M, j])
        R[k:M, j] = R[k:M, j] - 2.0 * np.dot(u, utA) 



#k = 0
#x = A[k:M,k].copy()
#x = x.reshape((1, len(x)))

#e = np.zeros(len(x))
#e[0] = 1
#x = np.array([[5, 0, 0, 0]])
#normval = np.linalg.norm(x)

#A[1:M, 0] = 555
#sign = cmp(-10, 0)