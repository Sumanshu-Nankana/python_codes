import cv2
import numpy as np

height = 512
width = 512
img = np.zeros([height, width, 3], dtype=np.uint8)

text = "WHITE"
org = (159,248)
fontFace = cv2.FONT_HERSHEY_PLAIN
fontScale = 2
color = (255,255,255)
thickness = 2
lineType = cv2.LINE_AA
img = cv2.putText(img, text, org, fontFace, fontScale, color,
                  thickness, lineType, bottomLeftOrigin=False)

window_name = 'Image'
cv2.imshow(window_name, img)

cv2.waitKey(0)
cv2.destroyAllWindows()