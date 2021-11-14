# how to load webcam 
# and how to use them 

import numpy as np
import cv2

#1. Displaying Video Capture Device

# cap: capture
#VideoCapture(number of webcams pr video device)
# VideoCapture(0 = first webcam)(1 = second webcam

# cap = cv2.VideoCapture(0) --> who has webcam

cap = cv2.VideoCapture(r'assets\hiphop.mp4') # who does not have webcam, so just take a mp4 video


# check if camera opened succeefully
if (cap.isOpened() == False):
    print('Error opening video stream or file')

# read until video is completed

while (cap.isOpened()):
    ret, frame = cap.read()
    
    # frame is going to read image, so frame is itself an image--a numpy array
    # ret = return  = return true or false: going to tell if webcam is working porperely or no
    if ret == True:
        # display the frame
        cv2.imshow('frame', frame)

        # press q on keyboard to exit
        # ord('q') = ordinal value/ASCII value of q
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

# when everything is doen, release the captured video

cap.release() 

# close all the frames 
cv2.destroyAllWindows()

'''
or simple code

cap = cv2.VideoCapture('hiphop.mp4')
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
            break 
cap.release() 
cv2.destroyAllWindows()

'''


#3. Mirrioring videos multiple times 

# create array with zeros and then pass fill it with image shape

cap1 = cv2.VideoCapture(r'assets\hiphop.mp4')
while True:
    ret, frame = cap1.read()
    # we also need heigth and widght of the image so that we can put our 4 frame there
    width = int(cap1.get(3)) # 3 for width in get() property 
    height = int(cap1.get(4)) # convert into int  value bcz by default it gives floating point
    
    image = np.zeros(frame.shape, np.uint8) ## assign frame shape and data type (uint8 - unsigned int 8bit)
    
    # if i want to mirror my self 4 times, then take original frame and shrink it by half (as half both side H and W so it can fit 4 images) it so that it can fit into windows
    smaller_frame = cv2.resize(frame,(0,0), fx = 0.5, fy =0.5)
    image[:height//2,:width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)# TOP LEFT, and  height :height//2 = smaller frame height 
    image[height//2:,:width//2] = smaller_frame # BOTTOM LEFT
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) # TOP RIGHT
    image[height//2:, width//2:] = smaller_frame # BOTTOM RIGHT 

    cv2.imshow("Mirrored Frame", image)
    if cv2.waitKey(1) == ord('q'):
        break
cap1.release()
cv2.destroyAllWindows()

