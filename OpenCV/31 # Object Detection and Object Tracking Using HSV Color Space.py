# We already see how to convert Color Image to GRAY Scale image
# There are more than 150 methods for color conversion in Open-cv.
# and one of them is 'Coloured Image to HSV'.

# What is HSV Color Space?

# HSV = (Hue, Saturation and value)

# Hue - corresponds to the color components (base pigment)
#       Hence, just by selecting  range of Hue, you can select any color (0-360 degree angle)

# Saturation - is the amount of color (depth of the pigment) (dominance of Hue) (0-100%)

# Value - is basically the brightness of the color (0-100%)

# Where color description plays a very important role - There we use HSV
# ============================================================================

import cv2
import numpy as np

while True:
    frame = cv2.imread('./data/smarties.png')

    #convert coloured image to HSV image
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define the lower and upper threshhold of Blue color in HSV
    lower_blue = np.array([110, 50, 50])    # lower limit of blue color
    upper_blue = np.array([130, 255, 255])  #upper limit of blue color

    # Threshold the HSV image to get only the Blue color
    # whereever the blue color present in image it get white and rest all are black
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    # the output is we only see blue color in image - rest all become black
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # But there are some noises in the result image,we will see later how to remove 
    # those noises.

    # Lets show all images (original, mask, result)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", res)

    key = cv2.waitKey(1)
    if key==27:
        break

cv2.destroyAllWindows()
