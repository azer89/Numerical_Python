
# permutation matrix

import numpy as np

N = 4
A = np.random.rand(N,N)

print "A"
print A, "\n"

I = np.identity(N)

new_order = [2, 3, 1, 0]
I = I[new_order, :]

print "I"
print I, "\n"
print " "

# swap
B = np.dot(I, A)
print "B"
print B, "\n"

#I = np.identity(N)
#new_order = [2, 3, 1, 0]
#I = I[:, new_order]
#print "I"
#print I, "\n"
#print " "
#
## swap
#C = np.dot(I, A)
#print "C"
#print C, "\n"