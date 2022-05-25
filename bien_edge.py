import cv2
import numpy as np

I=cv2.imread('Coins.jpg')
cv2.imshow("anh goc",I)
Ig=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
Ie=cv2.Canny(Ig,0,255)

# tìm biên theo SOBEL
sobelx = cv2.Sobel(I,ddepth=cv2.CV_64F, dx=1, dy=0, ksize=1)  # tìm biên sobel đạo hàm theo x
sobely = cv2.Sobel(I,cv2.CV_64F,0,1,ksize=1)  #  tìm biên sobel đạo hàm the y

# Tìm biên theo Laplacian và canny
laplacian = cv2.Laplacian(I,cv2.CV_64F) #tìm biên theo laplacian
Icanny = cv2.Canny(image=I, threshold1=100, threshold2=200) # tìm biên theo Canny 
cv2.imshow('candy',Icanny)
cv2.imshow('laplacian',laplacian)

# Lấy biên Sobel trung bình theo cả x và y
img_gaussian = cv2.GaussianBlur(Ig,(5,5),0)
 
img_sobelx = cv2.Sobel(img_gaussian,ddepth=cv2.CV_64F, dx=1, dy=0, ksize=1)  # tìm biên sobel đạo hàm theo x
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_64F,0,1,ksize=1)  #  tìm biên sobel đạo hàm the y

img_sobelx = np.uint8(np.absolute(img_sobelx))
img_sobely = np.uint8(np.absolute(img_sobely))

img_sobel = (img_sobelx + img_sobely)/2
for i in range(img_sobel.shape[0]):
    for j in range(img_sobel.shape[1]):
        if img_sobel[i][j] < 25:
            img_sobel[i][j] = 0
        else:
            img_sobel[i][j] = 255

cv2.imshow('anh sobelx',img_sobelx)
cv2.imshow('anh sobely',img_sobely)
cv2.imshow('anh sobel',img_sobel)

cv2.imshow("Anh bien",Ie)
cv2.waitKey()