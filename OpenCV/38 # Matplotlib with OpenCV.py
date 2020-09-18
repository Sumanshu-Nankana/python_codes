import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./data/lena.jpg', 1)

cv2.imshow('Image', img)

# display image using matplotlib
plt.imshow(img)
plt.show()

# But we will see color difference in both images
# reason: opencv read the image in BGR format
# matplotlib read the image in RBG format

cv2.waitKey(0)
cv2.destroyAllWindows()