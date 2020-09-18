# Morphological Transformations are some simple operations based on image shape.
# Morphological Transformations are normally performed on binary images.


import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('./data/smarties.png', 0)  # Load it as Gray Scale Image

# Normally we done morphological transformation on binary images
# So lets apply threshold
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# After masking, there are black dotes in between the ball
# lets suppose we want to remove those dots.
# For this we will use the dilation transformation

kernel = np.ones((2,2),np.uint8) 
# kernel is 2*2 sqaure shape we choose np.ones (as we want to apply white shape)

dilation = cv2.dilate(mask, kernel=kernel)
# we could notice that black dots inside the balls get reduced.
# but still we see some or small size black dots

dilation1 = cv2.dilate(mask, kernel=kernel, iterations=2)
# by default iteration is 1
# But still, we could see few black dotes
# one way is to increase the rectangel size of kernel
# it will remove the black dots, but there is a problem
# it will also increase the size of balls ; because size of kernel increases

#using erosion, size of balls get decreases, i.e. boundary get eroded
erosion = cv2.erode(mask, kernel=kernel, iterations=1)

# opening - is just another term for erosion by dilation 
# (i.e. first erosion and then dilation)
opening = cv2.morphologyEx(mask, op=cv2.MORPH_OPEN, kernel=kernel)

# opposite of opening i.e. first dilation and then erosion
closing = cv2.morphologyEx(mask, op=cv2.MORPH_CLOSE, kernel=kernel)

# another morphological operation are-
# morphological gradient is difference between dilation and erosion
morph_gradient = cv2.morphologyEx(mask, op=cv2.MORPH_GRADIENT, kernel=kernel)

titles = ['Image1', 'Masked Image', 'dilate image', 'dilate image1', 
           'Erosion', 'opening','closing', 'morphological gradient']
images = [img, mask, dilation, dilation1, erosion, opening, closing, morph_gradient]

for i in range(len(images)):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()