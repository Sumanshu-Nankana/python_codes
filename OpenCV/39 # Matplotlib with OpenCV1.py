import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./data/lena.jpg', 1)

cv2.imshow('Image', img)

# Lets convert BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()

# Now both the image looks same.

cv2.waitKey(0)
cv2.destroyAllWindows()