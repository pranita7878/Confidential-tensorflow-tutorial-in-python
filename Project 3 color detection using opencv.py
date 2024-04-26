import cv2
import numpy as np
 
 
 
 
 
img = cv2.imread(r'C:\Users\PRIDE PC\Desktop\pranita python code\circles.jpg')
 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
 
#Red color rangle  169, 100, 100 , 189, 255, 255
 
 
lower_range = np.array([169,100,100])
upper_range = np.array([189, 255, 255])
 
mask = cv2.inRange(hsv, lower_range, upper_range)
 
cv2.imshow('image', img)
cv2.imshow('mask', mask)
 
 
cv2.waitKey(0)
cv2.destroyAllWindows()

