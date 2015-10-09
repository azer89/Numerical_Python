
import numpy as np
from numpy import linalg as la

a_array = np.array([5.0, 4.0, 3.0, 2.0, 1.0])
an = a_array[0]
c_array = np.reshape(a_array[1:len(a_array)] / an, (1, len(a_array) - 1))
c_array = -c_array


r_zeros = np.zeros(len(a_array) - 2)
r_zeros = np.reshape(r_zeros, (len(r_zeros), 1))
id_mat = np.matrix(np.identity(len(a_array) - 2))
id_mat_extended = np.concatenate((id_mat, r_zeros), axis=1)

c_mat = np.concatenate((c_array, id_mat_extended), axis=0)

eigen_vals, eigen_vectors = la.eig(c_mat)