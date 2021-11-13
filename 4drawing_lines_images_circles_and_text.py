# draw: line, rectangle, circle, text

import numpy as np
import cv2


cap = cv2.VideoCapture('hiphop.mp4')
while True:
    ret, frame = cap.read()
    Width = int(cap.get(3))
    height = int(cap.get(4))

    #1. Drawing lines: give start(0,0) end (widght, height) coordinates for the lines
    
    img = cv2.line(frame,(0,0),(Width, height), (255,0,0), 10)
    # (255,0,0) : BGR value, 10: 10 pixel line thick 

    # draw another line: pass img (not frame) here as we are going to draw another line of already line draw image

    img = cv2.line(img,(0,height),(Width, 0), (0,255,0), 10)



    # 2. Draw rectangles 

    # corodinates: (top left and bottom right), color, line width or want to fill entire rectangele(-1)
    # lets take a corodantes start: (100,100), end: (200,200)
    img = cv2.rectangle(img,(100,100),(200,200), (255,255,0),-1 )


    #3. Draw Circle
    # corodinate: center position; (300,300)
    # color: (0,0,255)
    # radius: 60
    # thickness

    img = cv2.circle(img,(300,300),60, (0,0,255),-1 )


    #4. Draw text
    # TEXT 
    # font
    # font size(scale): any scaler value
    # text location: w= 300,height = heigth-10
    # color: (0,0,0)
    # line thickness
    # line type for text to look better: cv2.LINE_AA

    font= cv2.FONT_ITALIC
    img = cv2.putText(img,'This is Priyanka', (30,height-10), font, 1, (100,0,122),4, cv2.LINE_AA)





    cv2.imshow('Frame',img)

    if cv2.waitKey(0) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()