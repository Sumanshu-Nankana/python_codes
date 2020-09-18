# In previous code output
# But we can clearly see the divider line and we can easily say 
# half is apple and half is orange

# In Image Blending - We need to blend that divider line as well
# So we will use the image pyramid techniques
# We need to follow 5 steps -
# 1- Load both images
# 2- Find gaussian pyramid of apple and orange images
# 3- Find the laplacian pyramid
# 4- Join left half of apple and right half of orange in each level of Laplacian pyramid
# 5- Join image pyramids and reconstruct original image

import cv2
import numpy as np

# Load Images

apple = cv2.imread('./data/apple.jpg')
orange = cv2.imread('./data/orange.jpg')

# Generate gaussian pyramid for apple

apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# Generate gaussian pyramid for Orange

orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# Generate Laplacian pyramid for Apple
apple_copy = gp_apple[-1]  # take the last layer
lp_apple = [apple_copy]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_extended)
    lp_apple.append(laplacian)

# Generate Laplacian pyramid for Orange
orange_copy = gp_orange[-1] # take the last layer
lp_orange = [orange_copy]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_extended)
    lp_orange.append(laplacian)

# Add left and right half of images in each level
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n+=1
    cols, rows, channels = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# Recosutruct the image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_reconstruct, apple_orange_pyramid[i])

cv2.imshow("Apple", apple)
cv2.imshow("Orange", orange)
cv2.imshow("apple_orange", apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()


