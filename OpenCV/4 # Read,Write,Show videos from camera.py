import cv2

# Its argument can be either the device index or the name of a video file. 
# Device index is just the number to specify which camera. 
# Normally one camera will be connected (as in my case). 
# So I simply pass 0 (or -1). 
# You can select the second camera by passing 1 and so on. 
# After that, you can capture frame-by-frame. 

cap = cv2.VideoCapture(0)

while True:
    # ret will store True if it grabbed the frame
    # frame will store actual captured frame
    ret, frame = cap.read() 

    # display the resulting frame
    cv2.imshow('Frame', frame)

    # if we use waitKey(0) - we get still image
    # if we use waitKey(1) - we get video Frame
    if cv2.waitKey(1) & 0xff== ord('q'):
        break

# release the capture
cap.release()
cv2.destroyAllWindows()

# 1.waitKey(0) will display the window infinitely until any keypress 
# (it is suitable for image display).

# 2.waitKey(1) will display a frame for 1 ms, 
# after which display will be automatically closed

# So, if you use waitKey(0) you see a still image until you actually 
# press something
# while for waitKey(1) the function will show a frame for 1 ms only.