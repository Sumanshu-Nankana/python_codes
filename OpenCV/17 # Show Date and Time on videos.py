import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX
text = 'Width: ' + str(cap.get(3)) + ' '  + 'Height: ' + str(cap.get(4))
fontScale = 1
thickness = 2
color = (0, 255, 255)
org = (10, 50)
org1 = (10,80)

while cap.isOpened():
    ret, frame = cap.read()
    date = str(datetime.now()) # we define date inside while loop, so that it print current time
                               # if we define outside loop, then time will not change
    if ret:
        frame = cv2.putText(frame, text, org, font, fontScale, color, thickness)
        frame = cv2.putText(frame, date, org1, font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.imshow('Image', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()