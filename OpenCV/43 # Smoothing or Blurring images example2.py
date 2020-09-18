import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('./data/lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

homo_kernel = np.ones((5,5), np.float32)/25
homo_image = cv2.filter2D(img, ddepth=-1,kernel=homo_kernel)

blur = cv2.blur(img, (5,5))

gaus_blur = cv2.GaussianBlur(img, (5,5),sigmaX=0)

median_blur = cv2.medianBlur(img, 5) 

# we could see median-blur output is very clear

# Bilateral filter - This will remove the noise and preserve the edges as well
# but it's slow as compared to other filters
# So if we need to preserve the borders - then we can use bilateral filters

bilateral_filter = cv2.bilateralFilter(img,d=9, sigmaColor=75, sigmaSpace=75)
# d - is the diameter of each pixel neighbourhood

titles = ['Image', '2D convolution', 'Blur', 'gaussian blur', 'Median blur', 'Bilateral Filter']
images = [img, homo_image, blur, gaus_blur, median_blur, bilateral_filter]


for i in range(len(images)):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()