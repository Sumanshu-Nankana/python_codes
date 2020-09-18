# Image Gradient - is a directional change in the intensity or color in an image.
# There are several image gradient method available in opencv


import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('./data/sudoku.png', 0)

# Laplacian Gradient
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
# cv2.CV_64F is a 64 bit float data type
lap = np.uint8(np.absolute(lap)) # Now we take an absolute and convert to unit8 

# Sobel Gradient - Two types SobelX and SobelY
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) 
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1) 
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)


titles = ['Image', 'Laplacian Gradient', 'SobelX', 'SobelY', 'Sobel Combined']
images = [img, lap, sobelX, sobelY, sobelCombined]

for i in range(len(images)):
    plt.subplot(3,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
