# Lets take a user response
# if user press 'Esc' key - then Image window get destroyed
# if user press 'S' key - then Image will saved

import cv2
img = cv2.imread('./data/lena.jpg', 0)
cv2.imshow('image', img)
key = cv2.waitKey(0)

if key==27:   # 27 is the ASCII value of 'Esc' key
    cv2.destroyAllWindows() 
elif key==ord('s'):
    cv2.imwrite('lena_copy.png', img)

# https://theasciicode.com.ar/ascii-printable-characters/number-sign-ascii-code-35.html