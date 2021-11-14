# Face and Eye detection
# link: https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
# link: https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters
'''
Haar Cascade classifier: pre-trained classifier which will look into an image and try to find specific feature in an image 
Features: color, edges, corner, anything you could take from an image (not the entire image) is a feature

'''
import numpy as np
import cv2

cap = cv2.VideoCapture(r'assets\hiphop.mp4')

# CascadeClassifier(cv2.data.haarcascades: path to this classfier where they are store in cv2 + haarcascade_frontalface_default.xml: specific pre trained classifier)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

## face detection

while True:

    ret, frame = cap.read()

    # convert frame image into gray scale and pass it into face_cascade
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    ### FACE DETECTION

    # this below code will return location of all faces  
    faces = face_cascade.detectMultiScale(gray, 1.3, 5 ) # 5: minNeighbors- haar cascade will draw many rectangle to tell this is face 

    '''
    # 1.3 = scale factor: resizing the image at each iteration time so that haar cascade classifier can deal with image in the required shape.
    # haar cascade classfiers is trained on diffenet size of image so now when we are passing an image which shape is larger than the classfier is trained so 
    # current image shape has to match to the classfier trained image shape. so we will resize the current Image by 1.3 by each iteration
    
    - recommended scale factor value = 1.05 --> means image is going to resize by 5% in each iteration
    - lower scaler factor value: higher accuray: lower performaning algorithm
    - larger scaler factor value: lower accuray: faster performaning algorithm  
    '''

    for (x,y,w,h) in faces: # as faces is giving me an rectangle, I will draw and rectangle in my image
        # (x,y) : top left,  (x+w, y+h): bottom right
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 5)


        # pick area where to draw an rectangle: so grab face area in image and draw rectangle over it
        # and if we can find face area and then I will also find my eye area
        # ROI = region of interest 

        roi_gray = gray[y:y+h, x:x+w] # y(rows) first then x(columns) as (rows, columns)
        roi_color = frame[y:y+h, x:x+w]



        ### EYE DETECTION
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex,ey,ew,eh) in eyes: # ex = eye x, ey = eye y, ew = eye width, eh = eye height
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (255,0,0), 5)
            




    cv2.imshow('Frame', frame)

    if cv2.waitKey(0) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()