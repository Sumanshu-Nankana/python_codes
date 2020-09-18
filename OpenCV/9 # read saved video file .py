# lets read the output video file saved via program_no 8

import cv2

cap = cv2.VideoCapture('output.avi')

while cap.isOpened():
    ret, frame = cap.read()

    if ret==True:
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()

cv2.destroyAllWindows()