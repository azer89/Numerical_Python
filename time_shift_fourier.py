
"""

Time-shift Fourier 

"""

import numpy as np
import matplotlib.pylab as plt

"""
Calculate the delay between two signals f1 and f2 using cross-correlation.
To get a proper result, f1 and f2 should be periodic
"""
def GetDelay(f1, f2):    
    assert(len(f1) == len(f2))
    N = len(f1)
    
    F1 = np.fft.fft(f1)
    F2 = np.fft.fft(f2)
    
    # Tis is based on cross-correlation which can calculate the similarity of two signals 
    # where one of the two is delayed

    # We multiply the complex conjugate of F1 with F2 in the frequency domain
    # so that the operation is the cross-correlation operation in the time domain
    F1conj_F2 = np.conj(-F1) * F2
    
    # this is the cross-correlation of f1 and f2 (time domain)
    f1_cc_f2 = np.fft.ifft(F1conj_F2) 
    
    # the delay is located at the index where the similarity value is the greatest
    shift_value = np.argmax(np.absolute(f1_cc_f2)) / float(N)
    
    return shift_value

if __name__ == "__main__":
    sampling_rate = 100.0
    delta = 1.0 / sampling_rate
    x = np.arange(0, 1, delta)
    shift = -0.01
    freq = 1.0
    f1 = np.sin (2.0 * np.pi * freq * x)
    f2 = np.sin (2.0 * np.pi * freq * (x + shift))
    N = len(f1)
        
    F1 = np.fft.fft(f1)
    F2 = np.fft.fft(f2)
    
    # Calculate the delay
    shift1 = GetDelay(f1, f2)
    shift2 = GetDelay(f2, f1)
    
    plt.clf()
    
    plt.plot(x, f1, color="blue")
    plt.plot(x, f2, color="red")
    plt.show()

