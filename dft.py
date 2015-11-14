

import numpy as np
import sys


N = 10
k = N
n = N

x = np.arange(0, 1, 1.0 / float(N))

freq = 1.0
f = np.sin (2.0 * np.pi * freq * x)

#z = complex(3, 4)
#print z.real
#print z.imag

F = np.zeros(N, dtype=complex)

for k_iter in range(k):
    for n_iter in range(n):
        z = (-2.0 * np.pi * k_iter * n_iter) / float(N)
        
        if(abs(z) > sys.float_info.epsilon):
            F[k_iter] += complex(0, f[k_iter] * np.exp(z))
        else:
            F[k_iter] += complex(F[k_iter].real + f[k_iter], 0)
        