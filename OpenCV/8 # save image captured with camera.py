import cv2

cap = cv2.VideoCapture(0)

# we can check the fourcc code here https://www.fourcc.org/codecs.php
fourcc_code = cv2.VideoWriter_fourcc('X','V','I','D')

# Check if camera opened successfully
if (cap.isOpened() == False): 
    print("Unable to read camera feed")

# VideoWriter (need 4 parameters) 
# output file name
# fourcc code
# frame per milliseconds
# size of video (Height and width)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('output.avi', fourcc_code, 10.0, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()

    if ret==True:

        # Write the frame into the file 'output.avi'
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('Frame', frame)
        
        # Press 'q' on keyboard to stop recording
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

# When everything done, release the video capture and video write objects
cap.release()
out.release()

# close all the frames
cv2.destroyAllWindows()