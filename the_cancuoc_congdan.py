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
 
# Câu 3 (2 điểm). Chuyển ảnh Ig sang ảnh nhị phân Ib với ngưỡng quyết định nhị phân 90. Hiển thị ảnh nhị phân Ib.
# Câu 4 (1 điểm). Làm trơn ảnh Ig theo bộ lọc median với lân cận cửa sổ kích thước 5x5 thu được ảnh Im. Hiển thị ảnh kết quả Im.
# Câu 5 (1 điểm). Xác định ảnh biên Ie của ảnh Im sử dụng phương pháp Sobel. Hiển thị ảnh kết quả Ie.
# Câu 6 (1 điểm). Xác định các contour của ảnh Im và vẽ vị trí các contour lên ảnh gốc I ban đầu.
cv2.waitKey()
cv2.destroyAllWindows()