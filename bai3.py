import cv2

img = cv2.imread('1.jpg')
# Original Img
cv2.imshow('Anh goc', img)

print('Chieu cao', img.shape[0])
print('Chieu rong', img.shape[1])
print('So kenh', img.shape[2])

# Green Channel
cv2.imshow("Kenh G",img[:,:,1])

# Size
print("Kich thuoc: ", img.size)

# Resize
width = int(img.shape[1] * 0.5)
height = int(img.shape[0] * 0.5)
dim = (width, height)

img_resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Kich thuoc anh sau khi thay doi : ',img_resized.shape)
 
cv2.imshow("Anh da thay doi", img_resized)

# Gray Image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Anh xam', imgGray)

# Black/White Image
imgR = img[:,:,2]
cv2.threshold(imgR,90,255,cv2.THRESH_BINARY)
cv2.imshow('Anh trang den',imgR)

cv2.waitKey(0)
cv2.destroyAllWindows()