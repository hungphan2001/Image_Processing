import numpy as np
import cv2 

# 1.  Đọc và hiển thị ảnh I.
I=cv2.imread('Capture1.PNG')
cv2.imshow("anh goc",I)

# 2. Chuyển ảnh mầu I sang ảnh đa cấp xám (grayscale) theo công thức (0.39,0.5,0.11), được ma trận ảnh Ig. Hiển thị ảnh Ig. Xác định mức xám lớn nhất của ảnh Ig.
I_red = I[:,:,2]
I_green = I[:,:,1]
I_blue = I[:,:,0]
def toGray(I): 
    Ig=0.39*I_red+0.5*I_green+0.11*I_blue 
    Ig=Ig.astype(dtype='uint8') 
    return Ig 
I_gray = toGray(I) 
cv2.imshow('Anh xam I_gray',I_gray)
a= I_gray.max()
print('Max cua I_gray',a)
# 3. Lấy biên của ảnh Ig theo phương pháp Canny được ảnh biên Ie là ảnh nhị phân nền đen. Kiểm tra pixel có tọa độ dòng y=160, cột x=326 có là điểm biên của ảnh Ig theo phép dò biên Canny không?
#    3.1. Xác định ma trận gradient theo hướng y và theo hướng x của Ig sử dụng toán tử Sobel và hiển thị 2 ma trận kết quả. 
Icanny = cv2.Canny(image=I, threshold1=100,threshold2=200)  # tìm biên theo Canny
cv2.imshow('Icanny', Icanny)
(h, w, d) = I.shape
B, G, R = cv2.split(I)
 
if(Icanny[326][160]==255):
    print("Tọa độ [326,160] là điểm biên của ảnh")
else:
    print("Tọa độ [326,160] không phải là điểm biên của ảnh!")
 
#3.1
sobelx = cv2.Sobel(I_blue,ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)  # tìm biên sobel đạo hàm theo x
sobely = cv2.Sobel(I_blue,cv2.CV_64F,0,1,ksize=5)  #  tìm biên sobel đạo hàm the y
cv2.imshow('Sobelx',sobelx)
cv2.imshow('Sobely',sobelx)
print(sobelx)
print(sobely)
# 4.  Nhị phân ảnh Ig theo ngưỡng Otsu được ảnh nhị phân nền đen được ảnh Ib. Hiển thị ảnh Ib.
ret, Ib = cv2.threshold(I_gray, 180, 255, cv2.THRESH_OTSU)
cv2.imshow("Anh nhi phan nguong Otsu", Ib)
# 5. Xác định các đường contour của ảnh Ib, tìm giá trị max_cv là chu vi lớn nhất trong các contour trên. Vẽ các contours có chu vi lớn nhất lên ảnh gốc I với mầu bgr = (0,0,255). Hiển thị ảnh I.
# *** cv.arcLength(contour,True)
I_copy = I.copy()
contours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I_copy, contours, -1, (0,255,0), 3) #vẽ trên ảnh gốc
cv2.imshow("Contour",I_copy)

i = 0.0
for j in contours:
    chuvi = cv2.arcLength(j, True)
    if(chuvi > i):
        i = chuvi
print("chu vi lon nhat cua cac contours la :",i)
for contour in contours:
  if cv2.contourArea(contour) == i:
      cv2.drawContours(I, [contour], -1, (0,0,255), 3)
cv2.imshow('Anh goc moi',I)
# 6.  Sử dụng bút bi nét đậm, viết tay chỉ 1 chữ số (từ 0 đến 9), khoanh vùng chữ số được 1 ảnh, sử dụng ví dụ Paint brush, chuẩn hóa ảnh thành ảnh gray, kích thước 28x28(cao 28, rộng 28), ghi lại được 1 ảnh vidu.jpg. 
# Sử dụng OpenCV đọc ảnh vidu.jpg được ma trận ảnh I. Chuyển ảnh thành mảng 1 chiều x có 784 phần tử (784=28*28).
cv2.waitKey()
cv2.destroyAllWindows()