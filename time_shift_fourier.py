
"""

Time-shift Fourier 

"""

import numpy as np
import matplotlib.pylab as plt

sampling_rate = 100.0
delta = 1.0 / sampling_rate
x = np.arange(0, 1, delta)
shift = -0.75
freq = 3.0
f1 = np.sin (2.0 * np.pi * freq * x)
f2 = np.sin (2.0 * np.pi * freq * x + (shift))
N = len(f1)

F1 = np.fft.fft(f1)
F2 = np.fft.fft(f2)

plt.clf()
plt.subplot(2,1,1)
plt.plot(x, f1, color="blue")
plt.plot(x, f2, color="red")
plt.subplot(2,1,2)
plt.plot(x, np.real(F1), color="blue")
plt.plot(x, np.imag(F1), color="blue")
plt.plot(x, np.real(F2), color="red")
plt.plot(x, np.imag(F2), color="red")
plt.show()

