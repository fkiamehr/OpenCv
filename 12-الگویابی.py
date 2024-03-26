import cv2
import numpy as np 
 
img_bgr = cv2.imread('p1.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
 
img_template = cv2.imread('p2.jpg', 0)
w, h = img_template.shape[::-1]
 
res = cv2.matchTemplate(img_gray, img_template, cv2.TM_CCOEFF_NORMED)
threshhold = 0.6
 
loc = np.where(res >= threshhold)
 
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)
 
cv2.imshow('flower', img_bgr)
 
cv2.waitKey(0)