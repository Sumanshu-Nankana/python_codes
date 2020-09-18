# In previous code, we are decreasing the resolution one by one
# But we have one method called as gaussian pyramid

import cv2

img = cv2.imread('./data/lena.jpg')
layer = img.copy()
gaussian_pyramid = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)
    cv2.imshow(str(i), layer)

cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()