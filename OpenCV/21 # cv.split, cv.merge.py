import cv2

img = cv2.imread('./data/smarties.png') # img is numpy-ndarray

print(f'Shape of Image is: {img.shape}')     # (row,col,channel)
print(f'Size of Image is: {img.size}')       # row*col*channel
print(f'DataType of Image is: {img.dtype}')  
cv2.imshow('Image', img)

b,g,r = cv2.split(img)        # split the image to get B,G,R channels
img = cv2.merge((b, g, r))    # merge the B,G,R channels to get the image (Here No change in image)

cv2.imshow('Image1', img)

cv2.waitKey(0)
cv2.destroyAllWindows()