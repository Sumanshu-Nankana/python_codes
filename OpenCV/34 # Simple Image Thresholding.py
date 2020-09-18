# Thresholding is a segmentation technique used for seprating an object
# from its background

import cv2

img = cv2.imread('./data/gradient.png')

src = img
thresh_hold_value = 127
max_val = 255
type = cv2.THRESH_BINARY  # there are many types of it

_, th1 = cv2.threshold(src, thresh_hold_value, max_val, type)

# in this every pixel value of image get compared with 127
# if pixel value is < 127, then pixel value become 0
# if pixel value is > 127, then pixel value become 255

cv2.imshow("Original Image", img)
cv2.imshow("Threshold Image", th1)

cv2.waitKey(0)
cv2.destroyAllWindows()