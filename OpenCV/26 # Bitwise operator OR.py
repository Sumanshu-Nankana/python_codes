import cv2
import numpy as np

img1 = np.zeros((250,500,3), dtype=np.uint8) # generate black image
img1 = cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1) # generate a white rectangle inside black image

img2 = np.zeros((250,500,3), dtype=np.uint8) # black image
img2 = cv2.rectangle(img2, (250,0), (500,500), (255,255,255), -1) # half filled with white

bitOR = cv2.bitwise_or(img1, img2, dst=None, mask=None) 

# Black region = 0
# white region = 1

cv2.imshow('Image1', img1)
cv2.imshow('Image2', img2)
cv2.imshow('BITOR', bitOR)

cv2.waitKey(0)
cv2.destroyAllWindows()