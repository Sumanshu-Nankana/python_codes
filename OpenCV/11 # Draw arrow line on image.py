import cv2

img = cv2.imread('./data/lena.jpg')

img = cv2.arrowedLine(img, (0,0), (250,250), (0,255,0), 5)

cv2.imshow('Image', img)


cv2.waitKey(0)
cv2.destroyAllWindows()