# there is no such method called laplacian available in openCv
# laplacian pyramid formed using gaussian pyramid

import cv2

img = cv2.imread('./data/lena.jpg')
layer = img.copy()
gaussian_pyramid = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)

layer = gaussian_pyramid[-1] # get the last image (or top image of pyramid)
cv2.imshow('Upper level', layer)
laplacian_pyramid = [layer]

# Laplacian Pyramid - Is difference between gaussian_pyramid of that image 
# and its extended version

for i in range(5,0,-1):
    gaussian_extend = cv2.pyrUp(gaussian_pyramid[i])
    laplacian_pyramid = cv2.subtract(gaussian_pyramid[i-1], gaussian_extend)
    cv2.imshow(str(i), laplacian_pyramid)

# we could see only edges.
# gaussian and laplacian pyramid helps us to Blend the images
# and to re-construction of the images.c

cv2.waitKey(0)
cv2.destroyAllWindows() 