import cv2

image = cv2.imread("leesin.jpg")
window_name = 'Anh goc'
# cv2.imshow(window_name, image)
cv2.waitKey(0) 
#closing all open windows 
cv2.destroyAllWindows() 

print('Chiều cao:',image.shape[0])
print('Chiều rộng:',image.shape[1])
print('Số kênh:',image.shape[2])

# cv2.imshow('Kenh red: ', image[:,:,2])
# cv2.imshow('Kenh green: ', image[:,:,1])
# cv2.imshow('Kenh blue: ', image[:,:,0])
# cv2.waitKey(0) 
# #closing all open windows 
# cv2.destroyAllWindows() 


# #kich thuoc anh va so kenh
# (h, w, d) = image.shape
# print("width={}, height={}, depth={}".format(w, h, d))

# #in gia tri mau 1 diem anh
# (B, G, R) = image[50, 50]
# print("R={}, G={}, B={}".format(R, G, B))