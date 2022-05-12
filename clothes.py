import cv2
import numpy as np
 
#5e Đọc 1 ảnh vào biến bộ nhớ, hiển thị ảnh
I = cv2.imread('clother1.jpg')
cv2.imshow('anh_goc', I)
 
# Sử dụng hàm thư viện OpenCV chuyển đổi ảnh I sang biểu diễn màu HSV được ma trận ảnh Ihsv.
# Hiển thị kênh H. Xác định mức xám trung bình của kênh V.
Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV) 
cv2.imshow('Kenh H', Ihsv[:,:,0])
#cv2.imshow('Kenh S', Ihsv[:,:,1])
# cv2.imshow('Kenh V', Ihsv[:,:,2])
cv2.imshow('HSV', Ihsv)
print("Mức xám trung bình kênh V : ", np.mean(Ihsv[:, :, 2]))
 
# 5g. Không sử dụng hàm thư viện của OpenCV, viết 1 hàm gọi là bgr2hsv chuyển 1 ma trận ảnh I sang ảnh HSV để làm câu 5e.
def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    diff = cmax-cmin
    if cmax == cmin:
        h = 0
    elif cmax == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif cmax == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    elif cmax == b:
        h = (60 * ((r - g) / diff) + 240) % 360
    if cmax == 0:
        s = 0
    else:
        s = (diff / cmax) * 100
    v = cmax * 100
    return h, s, v
print(rgb_to_hsv(45, 215, 0))
# 5h. Gán các giá trị mức xám của kênh V của ảnh Ihsv đều trắng tuyệt đối.
imgv = Ihsv[:, :, 2]
w = imgv.shape[1]
h = imgv.shape[0]
def bgr2hsv(imgv):
    for i in range(h):
        for j in range(w):
            if imgv[i][j] != 255:
                imgv[i][j] = 255
    return imgv
cv2.imshow('5h', bgr2hsv(imgv))
# Sử dụng hàm thư viện của OpenCV chuyển đổi ngược Ihsv về biểu diễn BGR được ma trận ảnh I2.
# Hiển thị I2.
I2 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow('I2', I2)
 
cv2.waitKey()
cv2.destroyAllWindows()