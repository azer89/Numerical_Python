
'''
2D Inverse FFT Example
'''

import numpy as np
import matplotlib.pylab as plt

N = 10
F = np.zeros(shape=(N, N), dtype=complex)
F[0, 5] = complex(1.0)
F[5, 0] = complex(1.0)

f = np.fft.ifft2(F)

plt.clf()
plt.imshow(np.real(f), cmap="gray")