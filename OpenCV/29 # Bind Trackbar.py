import cv2
import numpy as np

img = np.zeros((300,512,3), dtype=np.uint8)
cv2.namedWindow('Image')

# callback function
def nothing(x):
    print(x)

# create trackbar
trackbarName = 'B'
windowName = 'Image'  # Same namedWindow which we created above
value = 0             # Initial Value
count = 255           # Final value
onChange = nothing    # Function which we need to call, whenever Trackbar value changes
cv2.createTrackbar(trackbarName, windowName, value, count, onChange)

# Lets create Two More TrackBar
cv2.createTrackbar('G', windowName, value, count, onChange)
cv2.createTrackbar('R', windowName, value, count, onChange)

while 1:
    cv2.imshow('Image', img)
    k = cv2.waitKey(1) & 0xff
    if k == 27:    # esc key = 27
        break

    # Get the trackbar value
    b = cv2.getTrackbarPos('B', 'Image')  # trackbarname, windowName (in which we have trackbar)
    g = cv2.getTrackbarPos('G', 'Image')
    r = cv2.getTrackbarPos('R', 'Image')

    # Set these values to image, and will change the black image to coloured image
    img[:] = [b, g, r]


cv2.destroyAllWindows()
