# Normally, we used to work with an image of constant size. 
# But in some occassions, we need to work with images of different resolution 
# of the same image. 
# For example, while searching for something in an image, like face, 
# we are not sure at what size the object will be present in the image. 
# In that case, we will need to create a set of images with different resolution 
# and search for object in all the images. 
# These set of images with different resolution are called Image Pyramids 
# (because when they are kept in a stack with biggest image at bottom and 
# smallest image at top look like a pyramid).

# There are two kinds of Image Pyramids. 
# 1) Gaussian Pyramid and 2) Laplacian Pyramids

import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('./data/lena.jpg')
lower_resolution = cv2.pyrDown(img)  # It reduces the resolution of image
lower_resolution1 = cv2.pyrDown(lower_resolution) # Further it reduce the resoution
higher_resolution = cv2.pyrUp(lower_resolution1) # it will increase the resolution of image

cv2.imshow('Image', img)
cv2.imshow('LowerResolution', lower_resolution)
cv2.imshow('LowerResolution1', lower_resolution1)
cv2.imshow('HigherResolution1', higher_resolution)

cv2.waitKey(0)
cv2.destroyAllWindows()
