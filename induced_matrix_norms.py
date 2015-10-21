
# matrix norms

# this is a reimplementation from Jeff Orchard's source code for CS770 Numerical Analysis

import sys
import numpy as np
import matplotlib.pyplot as plt

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
max_idx = get_max_idx(vals)
    
# plot
plt.plot(thetas, vals, color='blue')
plt.plot(thetas[max_idx], vals[max_idx], 'o', color='red')
plt.show()
