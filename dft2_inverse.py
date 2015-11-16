'''
2D inverse DFT
'''

import numpy as np
import matplotlib.pylab as plt

width = height = 10
F = np.zeros(shape=(width, height), dtype=complex)
F[0, 5] = complex(1.0)
F[5, 0] = complex(1.0)

f = np.zeros(shape=(width, height), dtype=complex)


for w in range(width):
    for h in range(height):
        for m in range(width):
            for n in range(height):
                f[w, h] += F[m, n] * np.exp(2.0j * np.pi * (float(w * m) / float(width) + float(h * n) / float(height)))
                        
plt.clf()
plt.imshow(np.real(f), cmap="gray")
