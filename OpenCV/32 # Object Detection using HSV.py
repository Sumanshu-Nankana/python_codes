# In previous code, we could see we use lower_bound and upper bound of blue color
# but it's not easy to remember the lower and upper bound
# So, we will use the trackbar

import cv2
import numpy as np

def nothing():
    pass

cv2.namedWindow("Tracking")

cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)  #Lower Hue
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)  #Lower Saturation
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)  #Lower Value

cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)  #Upper Hue
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)  #Upper Saturation
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)  #Upper Value


while True:
    frame = cv2.imread('./data/smarties.png')

    #convert coloured image to HSV image
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    lower_blue = np.array([l_h, l_s, l_v])    
    upper_blue = np.array([u_h, u_s, u_v])    

    # Threshold the HSV image to get only the Blue color
    # whereever the blue color present in image it get white and rest all are black
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    # the output is we only see blue color in image - rest all become black
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # But there are some noises in the result image,we will see later how to remove 
    # those noises.

    # Lets show all images (original, mask, result)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", res)

    key = cv2.waitKey(1)
    if key==27:
        break

cv2.destroyAllWindows()
