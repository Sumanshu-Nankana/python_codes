# In Simple thresholding - we are using a global threshold value
# i.e. every pixel value in an image compare with that threshold value

# But that may not be good in idea in all the conditions, where images has
# different lightning conditions  in different areas.

import cv2

img = cv2.imread('./data/sudoku.png')
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Original Image", img)
cv2.imshow("Threshold Image", th1) 

# So we could see one area is black and other area is visible
# it's because image has different illumination value at different regions.

cv2.waitKey(0)
cv2.destroyAllWindows()