import cv2

img = cv2.imread(r'assets\flower.png', -1) 


#1. IMAGE REPRESENTATION

'''
- what is an Image look like
- what is represented in an image and how do we display this image
- how does Computer interpret this image

'''

print(img) # got an numpy array which gives Image pixel 


# so when we print the image, it calls an numpy array

print(type(img)) # <class 'numpy.ndarray'>


# and on numpy array, we can call all the numpy functions
# shape(H,W,C) : row(H =height), columns(W = width), color channel (C) --> (row,column) = 1 pixel (RGB values or any color values)

print(img.shape)   # (H = 476, W = 400, C = 4)

'''
say if we have RGB(c=3): so either we write 3 times matrix : (476x400) (476x400) (476x400) --> 3d
or we write 1 time matrix: (476x400x3) --> 3d


so we have 4 channels means this is 4 dimensional array 
- each row has multiple columns--> here each row has 400 columns(Width) and each columns(pixel) has 4 color channel [0,0,0,0],[234,255,255,255]
- color value between 0(black)--255(white)

[[0,0,0,0],[234,255,255,255],[234,255,255,255],[234,255,255,255],.........till 400times]
[[234,222,234,122],[233,233,233,233]]
[]
.
.
.
.
till 476 rows

# opencv has BGR: [ B=234,G=255,R=255] B=[255,0,0], G =[0,255,0], R=[0,0,255]

# for example for 2x2 pixels
[[0,0,0,0],[234,255,255,255]]
[[0,0,0,0],[234,255,255,255]]

'''



# size: number of all pixels = H*W*C
print(img.size)    # 190400



#2. ACESS PIXEL VALUES


# check first row pixel values

print(img[0]) # or write print(img[0,:]) --> 0th row and all column
'''

[[ 90 108  95 255]
 [ 90 108  95 255]
 [ 97 117 105 255]
 ...
 [ 43 100  69 255]
 [ 37  94  63 255]
 [ 37  94  63 255]]

'''



## 257th row and middle pixel

print(img[257][45:400])  #or print(img[257,45:400])


## want a particular pixel

# print(img[257][300]) # [ 52 205 250 255]

# or acces row and column in single bracket

print(img[257,300]) # [ 52 205 250 255]


# want 0th row and 0th columns
print(img[0,0]) # [ 90 108  95 255]


# want oth column (means all row)
print(img[:,0])

'''
[[ 90 108  95 255]
 [ 90 108  95 255]
 [103 120 107 255]
 ...
 [122 125  99 255]
 [137 141 112 255]
 [137 141 112 255]]
'''

#3. CHANGING PIXEL COLORS

# look for first 100 rows
# look for all columns --> shape[2]

import random

for i in range(100):
    for j in range(img.shape[1]): # we are looking for columns here, shape: (row=0, columns=1, channels=2) so shape[1]--> gives columns
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255)] # 4 times becase we have 4 channels

# show image 
cv2.imshow("Pixel value changed image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
     

#4. COPY AND PASTE ONE PART OF IMAGE (part of array) INTO OTHER PART OF IMAGE

mask_copy = img[200:300, 345:400] # rows copy = 100 (300-200), columnc  copy = 55 (400-345)

# paste on this part --> remember dim same = number of rows and columns has to be same where we are going to copy
# so we need rows = 100, columns = 55

img[100:200, 145:200] = mask_copy
cv2.imshow("Copied image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
