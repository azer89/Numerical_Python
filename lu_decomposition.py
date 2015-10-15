
'''
LU Decomposition

Reza Adhitya Saputra
Computer Science Department - University of Waterloo
radhitya@uwaterloo.ca
'''

import numpy as np

'''
LU decomposition (not optimized)
'''
def lu_decomposition(mat) :
    n = len(mat[:,1])
    
    l_mat = np.eye(n)   
    u_mat = mat.copy()
    
    for k in range(0, n-1):     # pivot row
        for l in range(k+1, n): # rows below the pivot
            m = u_mat[l][k] / u_mat[k][k]
            u_mat[l][k] = 0
            for c in range(k+1, n): # column
                u_mat[l][c] = u_mat[l][c] - m * u_mat[k][c]
            l_mat[l][k] = m
        
    return l_mat, u_mat

#mat = np.array([[  1.0, 3.0, -11.0], 
#                [ -6.0, 7.0,  10.0], 
#                [-11.0, 2.0,  -2.0]])

mat = np.array([[  1.0, -2.0,   3.0], 
                [  2.0,  5.0,  12.0], 
                [  0.0,  2.0, -10.0]])

#mat = np.array([[  4.0, 3.0], 
#                [  6.0, 3.0]])

l_mat, u_mat = lu_decomposition(mat)

#row = len(mat[:,1])
#col = len(mat[1,:])   
                
