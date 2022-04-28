# Sử dụng Python và thư viện OpenCV (import cv2)
# 1. Đọc 1 ảnh vào biến bộ nhớ I. Hiển thị ảnh.
import cv2
import numpy
import numpy as np
I = cv2.imread('1.jpg')

# Original I
cv2.imshow('Anh goc', I)

# 2. Hiện thị chiều cao, chiều rộng, số kênh của ảnh. 
#  
print('Chieu cao', I.shape[0])
print('Chieu rong', I.shape[1])
print('So kenh', I.shape[2])
# 3. Hiện thị kích thước của ảnh

print("Kich thuoc: ", I.size)
# 4. Hiển thị giá trị pixel điểm ảnh tại tọa độ y=40 (dòng), x=15 (cột) của ảnh I.

print('I point : ', I[40, 15,:]) 
# 5. Resize ảnh nhỏ bằng 1/2 ảnh ban đầu.  Lưu thành anh.png
scale_percent = 50 # percent of original size
width = int(I.shape[1] * scale_percent / 100)
height = int(I.shape[0] * scale_percent / 100)
dim = (width, height)
  
resized = cv2.resize(I, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
# 6. Tách 3 kênh của ảnh I thành I_red, I_green, I_blue. Hiển thị ảnh kênh I_blue. 
I_red=I[:,:,2]
I_green=I[:,:,1]
I_blue=I[:,:,0]
# cv2.imshow('Kenh red: ', I_red[:,:,2])
# cv2.imshow('Kenh green: ', I_green[:,:,1])
# cv2.imshow('Kenh blue: ', I_blue[:,:,0])
# 7. Hiển thị giá trị pixel điểm ảnh tại tọa độ y=40 (dòng), x=15 (cột) của ảnh I_blue.
print('I blue : ', I_blue[40, 15]) 
# 8. Tính min, max giá trị mức xám của kênh green 

# print('Tong min',numpy.min(I[:,:,1]))
# print('Tong max',numpy.max(I[:,:,1]))
a= I_green.max()
b = I_green.min()
print('Max,Min',a,b)
# 9. Chuyển I thành ảnh xám I_gray sử dụng hàm có sẵn trong OpenCV.

Ig=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image',Ig)
# 10. Chuyển I thành ảnh xám I_gray2 bằng cách tự viết hàm.
# Công thức chuyển Y = 0.2126R + 0.7152G + 0.0722B
def toGray(I): 
    Ig=0.2126*I[:,:,2]+0.2126*I[:,:,1]+0.0722*I[:,:,0] 
    Ig=Ig.astype(dtype='uint8') 
    return Ig 
I_gray2 = toGray(I) 
cv2.imshow('Anh xam I_gray2',I_gray2)

# 11. Tính min, max giá trị mức xám của ảnh I_gray
c= Ig.max()
d= Ig.min()
print('Max,Min cua I_gray',c,d)
# 12. Hiển thị giá trị pixel điểm ảnh tại tọa độ y=40 (dòng), x=15 (cột) của ảnh  I_gray2. 
print('I gray 2 : ', I_gray2[40, 15]) 
# 13. Chuyển I_gray thành ảnh trắng đen I_bw với ngưỡng 90. Điều chỉnh ngưỡng (bằng 50 và 120),  hiển thị ảnh.
I_bw = Ig
cv2.threshold(I_bw,90,255,cv2.THRESH_BINARY)
cv2.imshow('Den trang ',I_bw) 
# 14. Chuyển I_red thành ảnh trắng đen I_bw2 với ngưỡng OTSU. Hiển thị ảnh và ngưỡng tìm được. 
I_bw2 = I_red
cv2.threshold(I_bw2,90,255,cv2.THRESH_OTSU)
cv2.imshow('Den trang 2 ',I_bw2) 
# 15. Chuyển I_gray thành ảnh trắng đen I_bw3 với ngưỡng GAUSSIAN …. 
I_bw3=Ig
ret, bina2 = cv2.threshold(I_bw2,90,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
cv2.imshow("GAUSSIAN : ",bina2)
# 16. Tính min, max giá trị mức xám của ảnh I_bw
e= I_bw.max()
f= I_bw.min()
print('Max,Min cua I_bw',e,f)
# 17. Hiển thị giá trị pixel điểm ảnh tại tọa độ y=40 (dòng), x=15 (cột) của ảnh  I_bw2
print('I bw 2 : ', I_bw2[40, 15]) 

cv2.waitKey(0)
cv2.destroyAllWindows()