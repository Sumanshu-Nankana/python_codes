import cv2
import numpy as np

img = cv2.imread('./data/lena.jpg')

def click_event(event, x, y, flags, param):

    # get the BGR color - where we clicked
    # and create a new image and filled the same with that selected color
    if event == cv2.EVENT_LBUTTONDOWN:
        
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]

        mycolorImage = np.zeros((512,512,3), dtype=np.uint8)
        mycolorImage[:] = [blue, green, red]
        cv2.imshow('New Color Image', mycolorImage)

cv2.imshow('Image', img)
cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()