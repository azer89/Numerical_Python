
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

# Fourier transform
F = np.fft.fft(f)

# we manipulate Fourier coefficients to obtain the derivative of f
F_edited = F.copy()

# I don't use fftshift, so I make my own omega array
bound1 = (N / 2) + 1
bound2 = N / 2

# the first half of omega
omega1     = np.arange(bound1) 
# the second half is the negative of the flipped array of the first half
omega2     = -np.flipud(omega1[1:bound2]) 
# the full array
omega_full =  np.concatenate((omega1, omega2))

# Calculate new coefficients
for i in range(len(omega_full)):
    omega = omega_full[i]
    F_edited[i] = 2.0j * np.pi * omega * F_edited[i]
  
# calculate the approx derivative
f_prime_approx = np.fft.ifft(F_edited) / N

# calculate the exact derivative
f_prime_exact = np.diff(f)

# for visualization purpose:
#     Because the length of f_prime_exact is N - 1, we need to shift the x-axis
#     by the half of the average of the space
shift_val = np.average(np.diff(x)) / 2.0

# display the result
plt.clf()
# plot the exact derivative
plt.plot(x[1:len(x)] - shift_val, f_prime_exact, color="blue", label="exact f'(x)")
# plot the real parts, since the imaginary parts are zero 
plt.plot(x, np.real(f_prime_approx), color="red", label="approx f'(x)")

plt.legend(loc='upper right', shadow=False)
plt.title("Finding derivatives using Fourier transform")
plt.show()
