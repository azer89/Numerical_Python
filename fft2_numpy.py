

'''
Reza Adhitya Saputra
radhitya@uwaterloo.ca

2D FFT Example using numpy.fft
'''


import numpy as np
import matplotlib
import matplotlib.pylab as plt


# http://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])    

img_col = matplotlib.image.imread("caesar_small.png")
img_gray = rgb2gray(img_col)

width, height = np.shape(img_gray)

'''
# show the original image
plt.imshow(img_col)
plt.clf()
plt.imshow(img_gray, cmap='gray') 
'''  

F = np.fft.fft2(img_gray) 

plt.clf()
plt.imshow(np.absolute(F)) 