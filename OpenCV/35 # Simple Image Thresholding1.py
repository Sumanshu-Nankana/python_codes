import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./data/gradient.png')

src = img
thresh_hold_value = 127
max_val = 255

_, th1 = cv2.threshold(src, thresh_hold_value, max_val, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(src, thresh_hold_value, max_val, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(src, thresh_hold_value, max_val, cv2.THRESH_TRUNC) # till threshold value ppixel value not changed
_, th4 = cv2.threshold(src, thresh_hold_value, max_val, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(src, thresh_hold_value, max_val, cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2,3,i+1),
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()