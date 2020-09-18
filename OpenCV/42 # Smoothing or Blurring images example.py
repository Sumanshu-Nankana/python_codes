import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('./data/water.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

homo_kernel = np.ones((5,5), np.float32)/25
homo_image = cv2.filter2D(img, ddepth=-1,kernel=homo_kernel)

blur = cv2.blur(img, (5,5))

gaus_blur = cv2.GaussianBlur(img, (5,5),sigmaX=0)

median_blur = cv2.medianBlur(img, 5) 

titles = ['Image', '2D convolution', 'Blur', 'gaussian blur', 'Median blur']
images = [img, homo_image, blur, gaus_blur, median_blur]

# we could see median-blur output is very clear

for i in range(len(images)):
    plt.subplot(3,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()