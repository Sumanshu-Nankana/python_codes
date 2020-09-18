import cv2

img_path = './data/lena.jpg'
img = cv2.imread(img_path)

text = 'Lena Image'
org = (41,67) # bottom left coordinate of text string
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2
color = (0,232,123)
thickness = 2
lineType = cv2.LINE_AA
img = cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType,
                  bottomLeftOrigin=False)

org = (5,207)
text = 'Bottom Left'
fontFace = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType,
                  bottomLeftOrigin=True)

window_name = 'Image'
cv2.imshow(window_name, img)

cv2.waitKey(0)
cv2.destroyAllWindows()
