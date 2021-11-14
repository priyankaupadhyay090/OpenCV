'''
OpenCV --> Open Source Computer Vision Library 
- used for image analysis, video analysis, image processing, image manipulation, 
Link: https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_tutorials.html

'''

import cv2

#1. load an image


# by default it will load an image into BGR (instead of RGB) color pattern
# we can choose option in which color pattern we want to load an image - grey scale, regular color image, without considering transparancy (NO aplha value)
# cv2.imread_color (-1): load a color image, any transparancy of image will be neglected. It is a dafault flag
# cv2_imread_grayscale (0): load image in grayscale mode
# cv2.imread_unchanged (1): load image as such incluing alpha channel

img = cv2.imread(r'assets\flower.png', -1)  # load in grayscale



#. show the image

cv2.imshow('Flower Image', img)

#. always close the windows after showing the image 

cv2.waitKey(0) # wait infinitly second to close to window --> we will not pass this line of code until we press a key. if we do waitkey(10) menas wait 10 sec to press key and then close the window

cv2.destroyAllWindows()





#2. RESIZE THE IMAGE

img_resize = cv2.resize(img, (400,400)) # resize into (400,400) dimension 
cv2.imshow("Resized Image", img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()




# lets say I dont want to type dimension and want to resized 
# the image into half/quater half of original image

img_resize1 = cv2.resize(img, (0,0), fx=2 , fy = 2) # for half fx=0.5, fy=0.5
cv2.imshow("Resized Image into double", img_resize1)
cv2.waitKey(0)
cv2.destroyAllWindows()





#3. ROTATE THE IMAGE
img_rotate = cv2.rotate(img,cv2.cv2.ROTATE_180) # or for 90 degree clock wise: cv2.cv2.ROTATE_90_COUNTERCLOCKWISE
cv2.imshow('180 Rotae image', img_rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()



#4. SAVE AN IMAGE

cv2.imwrite('assets\img_rotate.jpg', img_rotate)