import cv2

cap = cv2.VideoCapture(0)

# we can get the captured property (There are various properties)
width = cap.get(3)
height = cap.get(4)

print(f'Width is:{width} and Height is {height}')

# Similarly, we can set the cpatured property ; and it return True after setting.
cap.set(3, 800)  # property_number, value  (3 - is for width)
cap.set(4, 600)  # property_number, value  (4 - is for width)

# please note, if set any random number, it's not necessary it will set that number
# but, camera will automatically set to available resolution
# example if we set width and height to 3000 and 3000
# and we run the code, we could see - it displays 1280 and 720 - instead of 3000 and 3000

print(f'Width is:{cap.get(3)} and Height is {cap.get(4)}')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Image', gray_frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()



