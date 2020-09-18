import cv2

img = cv2.imread('./data/lena.jpg')

# Parameter - (image, start_point, end_point, color, thickness)

start_point = (200,180)   # represents the top left corner of rectangle 
end_point = (400,380) # represents the bottom right corner of rectangle
color = (0,255,0)
thickness = 2         # thikness = -1 (means fill the rectangle with same color)

img = cv2.rectangle(img, start_point, end_point, color, thickness)

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()