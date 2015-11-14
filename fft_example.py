'''
Plot frequency spectrum

http://glowingpython.blogspot.ca/2011/08/how-to-plot-frequency-spectrum-with.html
http://snowball.millersville.edu/~adecaria/ESCI386P/esci386-lesson17-Fourier-Transforms.pdf (page 21)
'''

#from numpy import sin, linspace, pi
import numpy as np
#import scipy as sp
import matplotlib.pylab as plt
#from pylab import plot, show, title, xlabel, ylabel, subplot
#from scipy import fft, arange

sampling_rate = 10.0   # sampling rate
x = np.arange(0, 1, 1.0 / sampling_rate)

freq = 1.0
y = np.sin (2.0 * np.pi * freq * x)

disturbance =  np.random.rand(len(y)) - 0.5

y += disturbance

#plt.clf()
#plt.plot(x, y, 'b')
#plt.show()

Y = np.fft.fft(y) #/ len(y)
Y_abs = np.absolute(Y)
#Y = Y[range(len(y) / 2)]
plt.clf()
plt.plot(x, np.absolute(Y), 'r') # print the magnitude
plt.show()