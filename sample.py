import cv2
import time

cap = cv2.VideoCapture(0)

ret, img = cap.read()

time.sleep(5)

ret, img = cap.read()

blur = cv2.blur(img, (3, 3))
hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)


cv2.imwrite("red_hsv_light.bmp", hsv)