import cv2

# Read Image #
#=======================#
# Syntax: cv2.imread(path, flag)

# There are three values of flag:

# 1 ==> loads a coloured image (cv2.IMREAD_COLOR) (default value)
# 0 ==> grayscale image  (cv2.IMREAD_GRAYSCALE)
# -1 ==> load image as such , including alpha channels (cv2.IMREAD_UNCHANGED)

# If the image cannot be read (because of missing file, improper permissions, 
# unsupported or invalid format) then this method returns an empty matrix.
# For valid image it returns a matrix which is a numpy array

img = cv2.imread('./data/lena.jpg', 0)
print(img)

# Display an Image #
#==========================
# Syntax: cv2.imshow(window_name, image)

# cv2.imshow() method is used to display an image in a window.

cv2.imshow('image', img)

# But when we run this, image pop up for a milli seconds and disappears

cv2.waitKey(5000)  # Its a keyboard binding function, show image for 5 sec

# use --> cv2.waitKey(0) --> to show image until user press any key

#closing all open windows 
cv2.destroyAllWindows() 

# Write Image #
# =============================
# Syntax: cv2.imwrite(filename, image)

# filename: A string representing the file name. The filename must include image format like .jpg, .png, etc.
# image: It is the image that is to be saved.
# Return Value: It returns true if image is saved successfully. 

cv2.imwrite('lena_copy.png', img)