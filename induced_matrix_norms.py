
# matrix norms

# this is a reimplementation from Jeff Orchard's source code for CS770 Numerical Analysis

import sys
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

# get the index of the biggest element
def get_max_idx(vals):
    max_val = sys.float_info.min
    max_idx = -1
    sz = len(vals)
    for i in range(0, sz):
        val = vals[i]
        if val > max_val:
            max_val = val
            max_idx = i
    return max_idx


# generate a random matrix
A = np.random.rand(2, 2) - 0.5

# induced matrix norm
# this is an implementation of p-norm:
# $\max_{ (\left \| z \right \|)_{p} = 1 } (\left \|  A z \right \|)_{p}$ 

vals = []
thetas = np.arange(0, np.pi, np.pi / 360.0) 
for theta in thetas:
    # 2-norm
    z = np.array([np.cos(theta), np.sin(theta)])
    vals.append(  np.linalg.norm(np.dot(A, z))  )
    
# the biggest element
max_idx = get_max_idx(vals) # can be replaced with argmax

plt.figure(1)
plt.clf()
plt.plot(thetas, vals)
    
# plot the induced matrix norm
plt.plot(thetas, vals, color='blue')
plt.plot(thetas[max_idx], vals[max_idx], 'o', color='red')
plt.show()

# here, z is random
B = A + A.T
plt.figure(2)
plt.clf()
for i in range(1000) :
    x = np.random.rand(2) - 0.5
    x = x / np.linalg.norm(x)
    y = np.dot(B, x)
    plt.plot(y[0],y[1],'.')


EVals, EVecs = np.linalg.eig(B)

V1 = EVals[0] * EVecs[:,0] # long
V2 = EVals[1] * EVecs[:,1] # short

plt.plot([0,V1[0]], [0,V1[1]])
plt.plot([0,V2[0]], [0,V2[1]])

plt.axis('equal')
plt.show()
