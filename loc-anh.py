from operator import irshift
import cv2
import numpy as np
I=cv2.imread('1.jpg')
cv2.imshow('anh goc',I)
w = I.shape[1]
h = I.shape[0]
Ir=I[:,:,2]
Ig=I[:,:,1]
Ib= I[:,:,0]

I_avg=np.zeros((h,w,3),dtype='uint8')
I_avg[:,:,2]=cv2.blur(Ir,(3,3))
I_avg[:,:,1]=cv2.blur(Ig,(3,3))
I_avg[:,:,0]=cv2.blur(Ib,(3,3))

cv2.imshow('lọc trung bình',I_avg)

I_med=np.zeros((h,w,3),dtype='uint8')
I_med[:,:,2]=cv2.medianBlur(Ir,3)
I_med[:,:,1]=cv2.medianBlur(Ig,3)
I_med[:,:,0]=cv2.medianBlur(Ib,3)
cv2.imshow("trung vị",I_med)

import random
matran_trongso= np.zeros((7,7),dtype='float32')
s=0.0
for i in range(7):
    for j in range(7):
        matran_trongso[i][j]=random.random()
        s=s+matran_trongso[i][j]

for i in range(7):
    for j in range(7):
        matran_trongso[i][j]=matran_trongso[i][j]/s

print(matran_trongso)
I_2 = cv2.filter2D(I,-1,matran_trongso)

cv2.imshow("Lọc trọng số",I_2)









cv2.waitKey(0)