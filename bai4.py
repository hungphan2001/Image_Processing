import cv2
img = cv2.imread('CMTND01.jpg')
# Original Img
cv2.imshow('Anh goc', img)

cv2.waitKey(0)
cv2.destroyAllWindows()