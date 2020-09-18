# Canny Edge Detection algorithm is composed of 5 steps:
# 1 - Noise reduction
# 2 - Gradient calculation
# 3 - Non-maximum suppression
# 4 - Double Threshold
# 5 - Edge Tracking by Hysteresis

# But there is inbuilt function 'Canny' in openCv for all above steps

import cv2
from matplotlib import pyplot as plt 

#img = cv2.imread('./data/messi5.jpg', 0)
img = cv2.imread('./data/sudoku.png', 0)
canny = cv2.Canny(img, threshold1=100, threshold2=200)

titles = ['Image', 'Canny']
images = [img, canny]

for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()