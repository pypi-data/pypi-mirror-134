from bncode import BNcode
import cv2

cv2.imwrite('test/bncode.png', BNcode.create(123456))
print(BNcode.scan(cv2.imread('test/bncode.png'),debug=True))
cam = cv2.VideoCapture(0)
while True:
    c,img = cam.read()
    print(BNcode.scan(img,debug=True))
    cv2.waitKey(1)