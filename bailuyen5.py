# Bài luyện 5 
# Đọc ảnh  I.
# 1. Hiển thị
# ảnh I.
import cv2
from cv2 import waitKey
import numpy as np
I = cv2.imread("anh5.jpg")
cv2.imshow("Anh goc",I)
# 2. Chuyển ảnh mầu I sang ảnh đa cấp xám với thành phần mầu (r,g,b) là  (0.39,0.5,0.11), được ma
# trận ảnh Ig. Hiển thị Ig. Tính mức xám trung bình của Ig.
I_red = I[:,:,2]
I_green = I[:,:,1]
I_blue = I[:,:,0]
def toGray(I): 
    Ig=0.39*I_red+0.5*I_green+0.11*I_blue 
    Ig=Ig.astype(dtype='uint8') 
    return Ig 
Ig = toGray(I) 
cv2.imshow('Anh xam Ig',Ig)
print("Mức xám trung bình kênh V : ", np.mean(Ig))
# 3. Chuyển  I sang dạng HSV được ảnh Ihsv. Xác định mức xám lớn nhất của kênh S của Ihsv.
Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV) 
cv2.imshow('HSV', Ihsv)
print("Mức xam lon nhat kênh S : ", np.max(Ihsv[:, :, 1]))
# 4. Nhị phân ảnh Ig theo ngưỡng Otsu được ảnh nhị phân nền đen được ảnh Ib.
# Hiển thị ảnh Ib.
Ib = Ig
cv2.threshold(Ib,90,255,cv2.THRESH_OTSU)
cv2.imshow('Den trang Otsu ',Ib) 
# 5. Xác định  contour của Ib, tìm giá trị max của contour có chu vi lớn nhất. Vẽ các contours có chu vi > max/5 lên ảnh gốc I với mầu (255,0,255). Hiển thị.
I_copy = I.copy()
contours, hierarchy = cv2.findContours(Ib,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I_copy, contours, -1,(0,255,0), 2)
cv2.imshow('anh contour cua Ib', I_copy)

max_arc = 0.0
for cnt in contours:
    if cv2.arcLength(cnt, True) > max_arc:
        max_arc = cv2.arcLength(cnt, True)

print('Max chu vi:', max_arc)

I_copy = I.copy()
for cnt in contours:
    if cv2.arcLength(cnt, True) > max_arc/5:
        cv2.drawContours(I_copy, [cnt], -1, (0,0,255),2)

cv2.imshow('anh contour có chu vi > max/5', I_copy)
cv2.waitKey()
cv2.destroyAllWindows()
