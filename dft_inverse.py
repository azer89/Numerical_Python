
'''
Inverse Discrete Fourier Transform
'''

import numpy as np
import matplotlib.pylab as plt

N = 200
F = np.zeros(N, dtype=complex)

F[5] = complex(1)

f = np.zeros(N, dtype=complex)
for k in range(N): 
    for n in range(N):
        f[k] += F[n] * np.exp(2.0j * np.pi * n * k / float(N))

f = f / float(N)
f_abs = np.absolute(f)

x = np.arange(0, 1, 1.0 / float(N))
plt.clf()
plt.plot(x, np.real(f), 'r') 
plt.show()