
"""
radhitya@uwaterloo.ca

this code is based on:
    http://math.stackexchange.com/questions/23192/eigenvalue-decomposition-singular-value-decomposition
"""

import sys
import numpy as np

# Real symmetric matrix
N = 4
A = np.random.rand(N, N) - 0.5
A = A + A.T


# Eigen decomposition
L, V = np.linalg.eig(A)

# SVD decomposition
U, S, V = np.linalg.svd(A)


diag_U = np.diag(U)
diag_V = np.diag(V)

print "diagonals"
print diag_U
print diag_V
print "\n"

# we know that the singular values are the magnitude of the eigen values.

# calculate eigen values from singular values
EVals = np.zeros(N)
eps = sys.float_info.epsilon * 1e3
for i in range(N):
    EVals[i] = S[i]
    d = np.abs(diag_U[i] + diag_V[i])
    print d
    if d < eps:
        EVals[i] = -EVals[i]
        

print "eigen values"
print L # sorted based on magnitudes
print EVals# not sorted

