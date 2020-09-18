import cv2

img1 = cv2.imread('./data/messi5.jpg')
img2 = cv2.imread('./data/opencv-logo.png')

print(f'Shape of img1 is: {img1.shape}')
print(f'Shape of img2 is: {img2.shape}')

# Now add both image
# If images are of different shape,size - we will get error that arrays are not of same size
# So, first we need to resize the images (if they are of different size - like in our case)

img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

new_image = cv2.add(img1, img2)  # Now both image will get merged

cv2.imshow('Add Image', new_image) 
cv2.waitKey(0)
cv2.destroyAllWindows()