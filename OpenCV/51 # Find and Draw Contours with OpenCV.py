# Contours can be explained simply as a curve joining all the continuous points
# (along the boundary), having same color or intensity. 
# The contours are a useful tool for shape analysis and object detection and recognition.

# For better accuracy, use binary images. 
# So before finding contours, apply threshold or canny edge detection.

import cv2

img = cv2.imread('./data/opencv-logo.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply threshold
ret, thresh = cv2.threshold(gray_img, 127, 255, 0)

# find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# contours is the python list and its a numpy array of boundary points of object
# hierarchy - contains information about topology

print("Number of contours: ", str(len(contours)))
print(contours[0])

# Draw contours

cv2.drawContours(img, contours, -1, (0,255,0), 3)
# -1 means draw all contours

cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()