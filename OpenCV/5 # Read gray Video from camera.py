import cv2

# Lets capture gray scale frame in video
# Just convert the frame from BGR to GRAY

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame', gray)
    if cv2.waitKey(1) & 0xff== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

