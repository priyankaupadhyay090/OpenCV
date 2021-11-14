# templare image: detect left shoe and ball

# template image: image we want to locate into base/original image
# it is also important that template image size are same/close size in the base image

import numpy as np
import cv2


#1. Loading Tempate and base image and load in gray scale(0)
# img = base image

# both should be resize on same scale 

img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0),(0,0), fx=0.6, fy=0.6)
template_img1 = cv2.resize(cv2.imread('assets/ball.png', 0),(0,0), fx=0.6, fy=0.6)
template_img2 = cv2.resize(cv2.imread('assets/shoe.png'),(0,0), fx=0.6, fy=0.6)

h, w = template_img1.shape # no color channel here as it is gray image

# template matching methods: try all methods and choose which gives the best results

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy() # i want to draw an rectangle, and we should not do it on original 

    result = cv2.matchTemplate(img2, template_img1, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_loc, max_loc)

    '''
    # matchTemplate() : it will take template image as a convolutuon filter and slide it throught the img2
    # result array value: if match exactly or near by: 1, if not: 0
    # so at the end we want to find biggest and smallest value LOCATION in result array, which can tell that which part of image is our match 

    img1 size - W,H (4,4)
    template img size - w,h(2,2)
    result array size: W-w+1, H-h+1 (3,3)

    '''

    # now when we got the min and max location, we need to draw a rectangle to tell that this is our match
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: # these 2 method gives min value, other method gives max val
        location = min_loc

    else: # methods other than cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED , gives max val
        location = max_loc
    
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# while running: you will see image 6times as it will check it on all 6 methods


# for template_img2, just replace template_img1 by template_img2 and it should work 