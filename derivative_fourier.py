
"""
Reza Adhitya Saputra
radhitya@uwaterloo.ca

Finding derivatives using Fourier transform
"""

import numpy as np
import matplotlib.pylab as plt

sampling_rate = 100.0
delta = 1.0 / sampling_rate
x = np.arange(0, 1, delta)


freq = 2.0
f = np.sin (2.0 * np.pi * freq * x)

N = len(f)

F = np.fft.fft(f)

F_edited = F.copy()

# I don't use fftshift, so I make my own omega array
bound1 = (N / 2) + 1
bound2 = N / 2

omega1      = np.arange(bound1)
omega2      = -np.flipud(omega1[1:bound2])
omega_shift =  np.concatenate((omega1, omega2))

for i in range(len(omega_shift)):
    omega = omega_shift[i]
    F_edited[i] = 2.0j * np.pi * omega * F_edited[i]
  
f_prime_approx = np.fft.ifft(F_edited) / N
f_prime = np.diff(f)

shift_val = delta / 2.0

plt.clf()
plt.plot(x[1:len(x)] - shift_val, f_prime, color="blue", label="exact f'(x)")
plt.plot(x, np.real(f_prime_approx), color="red", label="approx f'(x)")
plt.legend(loc='upper right', shadow=False)
plt.title("Finding derivatives using Fourier transform")
plt.show()
