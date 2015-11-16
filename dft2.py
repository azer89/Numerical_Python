'''
2D  DFT
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


F = np.zeros(shape=(width, height), dtype=complex)
for w in range(width):
    for h in range(height):
        for m in range(width):
            for n in range(height):
                F[w, h] += img_gray[m, n] * np.exp(-2.0j * np.pi * (float(w * m) / width + float(h * n) / height))
 
'''
# show the original image
plt.imshow(img_col)
plt.clf()
plt.imshow(img_gray, cmap='gray') 
'''    
plt.clf()
plt.imshow(np.absolute(F)) 


