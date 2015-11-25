
"""

Time-shift Fourier 

"""

import numpy as np
import matplotlib.pylab as plt

sampling_rate = 100.0
delta = 1.0 / sampling_rate
x = np.arange(0, 1, delta)
shift = -0.01
freq = 1.0
f1 = np.sin (2.0 * np.pi * freq * x)
f2 = np.sin (2.0 * np.pi * freq * (x + shift))
N = len(f1)

#noise1 =  np.random.rand(len(f1)) - 0.5
#f1 += noise1 * 0.005
#
#noise2 =  np.random.rand(len(f2)) - 0.5
#f2 += noise2 * 0.005

F1 = np.fft.fft(f1)
F2 = np.fft.fft(f2)

# The calculation is based on cross-correlation
# which is a method to calculate the similarity of two signals where
# one of the two is delayed by a certain amount of time

# since cross-correlation is "inverse" of convolution,
# we multiply the complex conjugate of F1 with F2
# Note that we are doing (element-wise) multiplication in the frequency domain
# so that this operation is the cross-correlation operation in the time domain
F1conj_F2 = F1.conjugate() * F2
F2conj_F1 = F2.conjugate() * F1
ifft_F1conj_F2 = np.fft.ifft(F1conj_F2)
ifft_F2conj_F1 = np.fft.ifft(F2conj_F1)
shift1 = np.argmax(np.absolute(ifft_F1conj_F2)) / float(N)
shift2 = np.argmax(np.absolute(ifft_F2conj_F1)) / float(N)

plt.figure(1)
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

#plt.figure(2)
#plt.clf()
#plt.plot(x, np.real(ifft_F1conj_F2), color="blue")
#plt.plot(x, np.imag(ifft_F1conj_F2), color="blue", linestyle="--")
#plt.show()

#plt.figure(3)
#plt.clf()
#plt.plot(x, np.real(ifft_F2conj_F1), color="red")
#plt.plot(x, np.imag(ifft_F2conj_F1), color="red", linestyle="--")
#plt.show()


