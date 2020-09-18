import cv2

# ROI  = Region of Interest

img = cv2.imread('./data/messi5.jpg')

cv2.imshow('Image', img)  # The original image as 1 ball

# Lets suppose our region of interest is ball and we want to place it somewhere else
# So first get the cordinates of ball (TopLeft and BottomRight)

ball = img[280:340, 330:390]   # Slice the particular pixels
img[273:333, 100:160] = ball

cv2.imshow('NewImage', img)

cv2.waitKey(0)
cv2.destroyAllWindows()