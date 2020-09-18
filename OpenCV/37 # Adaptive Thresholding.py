# So to solve probem in Simple Thresholding
# we go for adaptive thresholding i.e.
# calculate the threshold value for a smaller region
# so we will get different threshold for different regions.

# to apply adaptive thresholding, image should be loaded into gray scale mode

import cv2

img = cv2.imread('./data/sudoku.png', 0)  # 0 for gray-scale

# using this, threshold value is mean of neighboour hood area.
th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                            cv2.THRESH_BINARY, 11, 2)

# 11 - is the block-size i.e. neighbour size
# C=2 which is a constant

# there is another adaptive method - i.e. GAUSSIAN_C
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY, 11, 2)


cv2.imshow('Original Image', img)
cv2.imshow('Adaptive Threshold MEAN', th1)
cv2.imshow('Adaptive Threshold GAUSSIAN', th2)


cv2.waitKey(0)
cv2.destroyAllWindows()