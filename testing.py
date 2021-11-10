import cv2 as cv
import easyocr

reader = easyocr.Reader(['en'])

img = cv.imread("testing.png")
cv.imshow("Test", img)
cv.waitKey(0)

result = reader.readtext(img)
print(result)