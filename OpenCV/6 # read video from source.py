import cv2

cap = cv2.VideoCapture('data/vtest.avi')

# when we provide file_name; we need to use cap.isOpened() - to check if file path is okay
# or file index is okay

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('FRAME', frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
