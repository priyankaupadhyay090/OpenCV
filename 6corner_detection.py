# link: https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_shi_tomasi/py_shi_tomasi.html

# Shi Tomasi Corner Detector 
# function: cv2.goodFeaturesToTrack()

import numpy as np
import cv2
from matplotlib import pyplot as plt


### Draw corners 


img = cv2.imread(r'assets\chess_board.jpg') # it is quite large image, resize it
img = cv2.resize(img, (0,0), fx=0.75, fy=0.75)

# convert image into gray scale-- easy to detecorner in grayscale image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


##  after gray scale conversion, now run corner detection algorithm

# cv2.goodFeaturesToTrack(source image, numbers of best corners want to detect(lets take 100), degree of confidence of corners between 0 and 1 (1= 100% confidence that this is a corner, 0 = not confidence at all), minumim Euclidean distance betwene corners that return )
# 0.5 = if you are getting locaton which are not corener, increase this confidence and make it 0.8
# Eucledean dist between 2 corners must be larger than 10

corners= cv2.goodFeaturesToTrack(gray, 100, 0.5, 10)
print(corners) # float data type but we need int to draw corners
corners = np.int0(corners)


for corner in corners:
    # print(corner)# we have 2d array 
    # we need to flat our array to get x and y corner

    x,y = corner.ravel() # [[[1],[2,3]]] --> flat : [1,2,3]

    # lets draw corner now after getting x and y value
    cv2.circle(img, (x,y),8, (0,0,255),-1)



### draw line bwtween corners. each corner connect to all corners

for i in range(len(corners)):
    for j in range(i+1, len(corners)): # it will loop those corner which i has not looped 
        corner1 = tuple(corners[i][0]) # convert into tuple bcz by default they are list
        corner2 = tuple(corners[j][0]) #[0] bcz we have flaten the array, [0] will first index only(x,y)
        
        # color = np.random.randint(0,255, size =3) # size=3 -> (0,0,0)
        # problem with above is that it gives int64 but but we want int8 bit
        # so we need to MAP then into int and then convert them into tuple
        color = tuple(map(lambda x: int(x), np.random.randint(0,255, size =3)))
        
        cv2.line(img, corner1, corner2, color, 1)




cv2.imshow('Chess Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()




