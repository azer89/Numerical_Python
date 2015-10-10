
import numpy as np
from numpy import linalg as la

'''
Find all roots of a polynomial:

a_{n} x^{n} + a_{n-1} x^{n-1} + a_{n-2} x^{n_2} + ... + a_{1} x + a_{0}

'''

# An array of a_{n}, a_{n-1}, ..., a_{0}
a_array = np.array([5.0, 4.0, 3.0, 2.0, 1.0])

# the value of a_{n}
an = a_array[0]

# normalized a_array
c_array = np.reshape(a_array[1:len(a_array)] / an, (1, len(a_array) - 1))

# negative
c_array = -c_array

# here we want to create C matrix, where C . x = lambda . x
r_zeros = np.zeros(len(a_array) - 2)
r_zeros = np.reshape(r_zeros, (len(r_zeros), 1))
id_mat = np.matrix(np.identity(len(a_array) - 2))
id_mat_extended = np.concatenate((id_mat, r_zeros), axis=1)
c_mat = np.concatenate((c_array, id_mat_extended), axis=0)

# obtain the eigen values and the eigen vector
eigen_vals, eigen_vector = la.eig(c_mat)