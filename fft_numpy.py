'''
Fast fourier transform using numpy.fft

http://glowingpython.blogspot.ca/2011/08/how-to-plot-frequency-spectrum-with.html
http://snowball.millersville.edu/~adecaria/ESCI386P/esci386-lesson17-Fourier-Transforms.pdf (page 21)
'''

import numpy as np
import matplotlib.pylab as plt

sampling_rate = 10.0
x = np.arange(0, 1, 1.0 / sampling_rate)

freq = 1.0
y = np.sin (2.0 * np.pi * freq * x)

disturbance =  np.random.rand(len(y)) - 0.5

Y = np.fft.fft(y)
Y_abs = np.absolute(Y)

plt.clf()
plt.plot(x, np.absolute(Y), 'r')
plt.show()