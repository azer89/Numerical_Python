
'''

permutation matrix demo which shows how to swap rows or colums

Swap rows:
    B = PA

Swap columns:
    B = AP

where A is the input matrix and P is a permutation matrix

'''

import numpy as np

## In[]:
#
#N = 4
#A = np.random.rand(N,N)
#
#print "A"
#print A, "\n"
#
## In[]:  swap rows
#I = np.identity(N)
#new_order = [2, 3, 1, 0]
#I = I[new_order, :]
#
#print "I"
#print I, "\n"
#print " "
#
#B = np.dot(I, A)
#print "B"
#print B, "\n"

# In[]: swap columns
N = 4
M = 6
A = np.random.rand(M,N)
I = np.identity(N)
new_order = [2, 3, 1, 0]
I = I[:, new_order]
print "I"
print I, "\n"
print " "

C = np.dot(A, I)
print "C"
print C, "\n"