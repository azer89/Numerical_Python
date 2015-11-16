
'''
Discrete Fourier Transform
'''

import numpy as np
import matplotlib.pylab as plt

N = 10

x = np.arange(0, 1, 1.0 / float(N))

freq = 1.0
f = np.sin (2.0 * np.pi * freq * x)

F = np.zeros(N, dtype=complex)
for k in range(N): 
    for n in range(N):
        F[k] += f[n] * np.exp(-2.0j * np.pi * n * k / float(N))

F_abs = np.absolute(F)

plt.clf()
plt.plot(x, F_abs, 'r') # print the magnitude
plt.show()