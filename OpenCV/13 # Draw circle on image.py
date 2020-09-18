import cv2

img = cv2.imread('./data/lena.jpg')

center = (307,264)
radius = 100
color = (198, 52, 235)
thickness = 2
img = cv2.circle(img, center, radius, color, thickness)

window_name = 'Image'
cv2.imshow(window_name, img)

cv2.waitKey(0)
cv2.destroyAllWindows()