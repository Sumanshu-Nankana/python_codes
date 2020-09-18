# importing cv2
import cv2

# Reading an image in default mode
img = cv2.imread('./data/lena.jpg')

# Lets draw a lines, So we will overwrite the same image, before showing it
# below are the parameters
# image on which line needs to be draw
# starting point_1 (in form of tuple)
# ending point_2 (in form of tuple)
# color in form of BGR (tuple)
# thickness (starting from 1...to...)

# Using cv2.line() method 
# Draw a blue line with thickness of 3 px
img = cv2.line(img, (0,0), (250,250), (255,0,0), 3)

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()