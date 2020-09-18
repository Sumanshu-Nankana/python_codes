# Track an object in Live Video

import cv2
import numpy as np

def nothing():
    pass

cap = cv2.VideoCapture(0)  # captured the video using live camera

cv2.namedWindow("Tracking")

cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)  #Lower Hue
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)  #Lower Saturation
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)  #Lower Value

cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)  #Upper Hue
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)  #Upper Saturation
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)  #Upper Value

while True:
    _, frame = cap.read()

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

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", res)

    key = cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()
