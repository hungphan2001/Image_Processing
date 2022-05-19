from itertools import count
import cv2
import numpy as np

# Trên ngôn ngữ C++ hoặc C#. Java và Python, sử dụng thư viện của OpenCV, viết chương trình thực hiện yêu cầu sau:
# Đọc ảnh the_cancuoc_congdan.jpg vào biến ma trận I.
# Câu 1 (2 điểm). Hiển thị ảnh, hiển thị kênh R của ảnh I.
I = cv2.imread('the_cancuoc_congdan.jpg')
print("Hien thi anh của I : ")
cv2.imshow('anh_goc', I)

print("Hien thi kenh R của I : ")
# print('Chiều cao:',I.shape[0])
# print('Chiều rộng:',I.shape[1])
# print('Số kênh:',I.shape[2])
cv2.imshow('Kenh red: ', I[:,:,2])
# Câu 2 (3 điểm). Chuyển ảnh sang ảnh grayscale được ảnh Ig mà không dùng hàm thư viện của OpenCV và hiển thị ảnh Ig.
def anhXam(img):
    imageHeight = img.shape[0]
    imageWidth = img.shape[1]
    Ig = np.empty([imageHeight, imageWidth], dtype = np.uint8) #uint8 số nguyên 8bit ko dấu
    for i in range(imageHeight):
        for j in range(imageWidth):
            Ig[i][j] = int(img[i][j][0]*0.2126 + img[i][j][1]*0.7152 + img[i][j][2]*0.0722)
    return Ig
Ig = anhXam(I) 
# Câu 3 (2 điểm). Chuyển ảnh Ig sang ảnh nhị phân Ib với ngưỡng quyết định nhị phân 90. Hiển thị ảnh nhị phân Ib.
(nguong, Ib) = cv2.threshold(Ig, 90, 255, cv2.THRESH_BINARY)
cv2.imshow('anh nhi phan nguong 90', Ib)
# Câu 4 (1 điểm). Làm trơn ảnh Ig theo bộ lọc median với lân cận cửa sổ kích thước 5x5 thu được ảnh Im. Hiển thị ảnh kết quả Im.
# Kenh R
Ir = I[:,:,2]
# Kenh G
Ig = I[:,:,1]
# Kenh B
Ib = I[:,:,0]
h=I.shape[0]
w=I.shape[1]
####lọc median (trung vị) 
I_med=np.zeros((h,w,3),dtype='uint8')
I_med[:,:,2]=cv2.medianBlur(Ir,5)
I_med[:,:,1]=cv2.medianBlur(Ig,5)
I_med[:,:,0]=cv2.medianBlur(Ib,5)
cv2.imshow('Loc median', I_med)
# Câu 5 (1 điểm). Xác định ảnh biên Ie của ảnh Im sử dụng phương pháp Sobel. Hiển thị ảnh kết quả Ie.
sobelx = cv2.Sobel(I_med,ddepth=cv2.CV_64F,dx=1,dy=0,ksize =5)
sobely = cv2.Sobel(I_med,cv2.CV_64F,0,1,ksize=5)
cv2.imshow('Solelx',sobelx)
cv2.imshow('Solely',sobely)
# Câu 6 (1 điểm). Xác định các contour của ảnh Im và vẽ vị trí các contour lên ảnh gốc I ban đầu.
xam = cv2.cvtColor(I,cv2.COLOR_BGR2RGB)
rett,gray = cv2.threshold(xam,127,255,0)
contours,hierachy= cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
img_co=cv2.drawContours(I,contours,-1,(0,255,0),3)
cv2.imshow('imgdraw',img_co)
cv2.waitKey()
cv2.destroyAllWindows()