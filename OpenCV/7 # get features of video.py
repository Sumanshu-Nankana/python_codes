# You can also access some of the features of this video using cap.get(propId) 
# method where propId is a number from 0 to 18. 
# Each number denotes a property of the video (if it is applicable to that video) 
# Some of these values can be modified using cap.set(propId, value).
# Value is the new value you want.
# For example, I can check the frame width and height by cap.get(3) and cap.get(4). 
# It gives me 640x480 by default. 
# But I want to modify it to 320x240. J
# ust use ret = cap.set(3,320) and ret = cap.set(4,240).

import cv2

cap = cv2.VideoCapture('data/vtest.avi')

while cap.isOpened():
    ret, frame = cap.read()
    
    width = cap.get(3)
    width1 = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # another way to get width

    height = cap.get(4)
    height1 = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # another way to get height
    
    cv2.imshow('FRAME', frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

print(f"Width:{width}, Height:{height}")
print(f"Width:{width1}, Height:{height1}")
cap.release()
cv2.destroyAllWindows()


# All the properties - 
# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get