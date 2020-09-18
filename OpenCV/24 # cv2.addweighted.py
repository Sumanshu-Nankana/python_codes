import cv2

img1 = cv2.imread('./data/messi5.jpg')
img2 = cv2.imread('./data/opencv-logo.png')

print(f'Shape of img1 is: {img1.shape}')
print(f'Shape of img2 is: {img2.shape}')

img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# Add weighted is for like - if we want to give 90% weight to 1st image
# and 10% weight to 2nd image 
# then we can use addWeighted()
new_image = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)  # src1, alpha, src2, beta, gamma

cv2.imshow('Add Image', new_image) 
cv2.waitKey(0)
cv2.destroyAllWindows()