# colors and color detection


# taks: convert frame color (BGR) into HSV color , HSV: Hue , Saturation and Brightness
# to extract color from image- done by HSV

import numpy as np
import cv2

cap = cv2.VideoCapture(r'assets\hiphop.mp4')
while True:
    ret, frame = cap.read()
    Width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # which color want  to extract:
    # lower bound and upper bound of pixel
    # 2 HSV colors define

    lower_blue = np.array([90,50,50]) # lighter blue
    upper_blue = np.array([130,255,255]) # darker blue


    # create an mask/part of image now
    # it will return to a new image/mask: which has only blue pixel exist, all other pixel which are not blue will be blacked out(black color)
    # so mask tell whcih pixel which should keep and which pixel we should not


    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # bitwise_and: 11=1, 01=0, 10=0, 00=1 --> so we only get 1 when both value are one, means when both frame has matching pixel, it will return those pixel , else will be black 

    result = cv2.bitwise_and(frame, frame, mask= mask)

    cv2.imshow("Frame", result)

    # can also see the mask image # so mask 1: for all blue pixel, mask 0: all other color pixel
    cv2.imshow("Mask", mask)

    if cv2.waitKey(0) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


'''
make yor own pixel color:

# creats array as an image means 4 channel [[[[255,0,0]]]]


BGR_COLOR = np.array([[[[255,0,0]]]])
x = cv2.cvtColor(BGR_COLOR, cv2.COLOR_BGR2HSV)
x[0][0] # 1 pixel

'''