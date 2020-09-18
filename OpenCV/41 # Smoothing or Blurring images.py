# Smoothing (also known as Blurring) - is most commonly used operation used in image processing.
# most common operation is removing noise from the images

# and we can achieve smoothing by using diverse Linear Filter (because they are fast)
# But there are various kind of filters available
# homogenous, Gaussian, Median, Bilateral filter

# Homogenous filter - is the most simple filter, each output pixel is the mean of its
#                     kernel neighbours
# In homogenous filter kernel = 1/ (width*height) * kernel_matrix
# So if we want to use use kernel of 5*5  = 1/25 * kernel_matrix

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('./data/opencv-logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# in original image - we have little bit noise on corners of text

homo_kernel = np.ones((5,5), np.float32)/25
homo_image = cv2.filter2D(img, ddepth=-1,kernel=homo_kernel)
# ddpeth = desired depth
# after applying filter2D - we could see corners are smoothen

# Low pass filter - helps in removing noise
# High pass filter - helps in finding edges in images
blur = cv2.blur(img, (5,5))
# blur method - also called as averaging

# There are more functions
# gaussian filter - is using different weight kernel in both x and y direction
# So pixel located on center has higher weight
# and pixel located on side has lower weight

gaus_blur = cv2.GaussianBlur(img, (5,5),sigmaX=0)
# gaussian blur is used to remove high frequency noise

# median filter - replace each pixel value with median of its neighbour
# It's good to remove salt-and-pepper noise on images

median_blur = cv2.medianBlur(img, 5) # here kernel size should be odd number (except 1)

titles = ['Image', '2D convolution', 'Blur', 'gaussian blur', 'Median blur']
images = [img, homo_image, blur, gaus_blur, median_blur]

for i in range(len(images)):
    plt.subplot(3,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()