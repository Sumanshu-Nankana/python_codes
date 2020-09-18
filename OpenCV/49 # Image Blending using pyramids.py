# Blending - means mixing

# One application of Pyramids is Image Blending. 
# For example, in image stitching, you will need to stack two images together, 
# but it may not look good due to discontinuities between images. 
# In that case, image blending with Pyramids gives you seamless blending without 
# leaving much data in the images. 
# One classical example of this is the blending of two fruits, Orange and Apple.

import cv2
import numpy as np

apple = cv2.imread('./data/apple.jpg')
orange = cv2.imread('./data/orange.jpg')

print(f"Apple Shape :{apple.shape}")
print(f"Orange Shape :{orange.shape}")

cv2.imshow('Apple', apple)
cv2.imshow('Orange', orange)

# One method is - we can cut half apple image and cut half orange image
# and then join both

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))
cv2.imshow('Apple_Orange', apple_orange)

# But we can clearly see the divider line and we can easily say 
# half is apple and half is orange
# In Image Blending - We need to blend that divider line as well
# So we will use the image pyramid techniques
# In next code....


cv2.waitKey(0)
cv2.destroyAllWindows()