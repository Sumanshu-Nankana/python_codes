import cv2
import numpy as np

# Lets create image using numpy 
height = 512
width = 512
img = np.zeros([height, width, 3], dtype=np.uint8)

# Mouse events are like -
# Left click, Right Click, double click..etc..

# let get all events available in cv2 libraray
# events = [e for e in dir(cv2) if 'EVENT' in e]
# print(events)

def click_event(event, x, y, flags, param):
    
    # To get (x,y) cordinate
    if event == cv2.EVENT_LBUTTONDOWN:
        text = '('+ str(x) + ' ' + str(y) + ')'
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (x, y), font, 1, (255,255,0), 2)
        cv2.imshow('Image', img)
    
    # To get BGR of that cordinate
    # As we have Black, image - so we will get (0,0,0) everytime
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        text = '(' + str(blue) + ',' + str(green) + ',' + str(red) + ')'
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (x, y), font, 1, (0,255,255), 2)
        cv2.imshow('Image', img)


cv2.imshow('Image', img)
cv2.setMouseCallback('Image', click_event) # Window Name should be same everywhere
cv2.waitKey(0)
cv2.destroyAllWindows()

# though we have not define 'x' and 'y' it automatically get the cordinates



