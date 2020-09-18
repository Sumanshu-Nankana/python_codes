import cv2
import numpy as np

img = np.zeros((512,512,3), dtype=np.uint8)

def click_event(event, x, y, flags, param):

    # to draw a very small circle (to indicate point)
    if event == cv2.EVENT_LBUTTONDOWN:
        
        radius = 3
        color = (0,255,255)
        cv2.circle(img, (x, y), radius, color, thickness=-1)

        # Store all clicked points in a list
        points.append((x, y))

        # and connect last 2 points
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0,255,0), thickness=2)
        cv2.imshow('Image', img)

cv2.imshow('Image', img)
points = []
cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()