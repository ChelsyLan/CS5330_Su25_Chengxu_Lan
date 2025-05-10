import cv2
import sys
import imutils
import numpy as np

img = cv2.imread("alice.jpg")

if img is None:
    sys.exit("Could not read the image.")

(h, w, d) = img.shape
print("width=", w, "height=", h, "depth=", d)

# press key to continue
# 1. show ROI
roi = img[20:320, 40:340]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# 2. Adjust the image size to (150, 150)
resized_img = cv2.resize(img,(150,150))
cv2.imshow('resized image',resized_img)
cv2.waitKey(0)

# 3. rotate image 45 degrees
center = (h//2,w//2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
cos = np.abs(M[0, 0])
sin = np.abs(M[0, 1])
new_w = int((h * sin) + (w * cos))
new_h = int((h * cos) + (w * sin))
M[0, 2] += (new_w / 2) - center[0]
M[1, 2] += (new_h / 2) - center[1]
rotated_img = cv2.warpAffine(img,M,(new_w,new_h))
cv2.imshow("rotated",rotated_img)
cv2.waitKey(0)

# 4. smooth image
blurred = cv2.GaussianBlur(img,(25,25),sigmaX=0)
cv2.imshow("blurred",blurred)
cv2.waitKey(0)

# 5. draw one rectangle, one circle, one line
drawed = img.copy()
yellow = (0,255,255)
cv2.rectangle(drawed,(50,50),(150,150),color=yellow,thickness=4)
cv2.circle(drawed,center=(300,100),radius=50,color=yellow,thickness=2)
cv2.line(drawed,(50,300),(50,800),color=yellow,thickness=3)
cv2.imshow("draw",drawed)
cv2.waitKey(0)

# 6. add text your name
text_img = img.copy()
cv2.putText(text_img,"Chengxu Lan",(100,200),cv2.FONT_HERSHEY_COMPLEX,0.5,yellow,1)
cv2.imshow("with text",text_img)
cv2.waitKey(0)

# 7. grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray scale",gray_img)
cv2.waitKey(0)

# 8. edge detection
edges = cv2.Canny(gray_img,100,200)
cv2.imshow("edge",edges)
cv2.waitKey(0)

# 9. apply threshold
_, thresh_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("apply threshold",thresh_img)
cv2.waitKey(0)

# 10. identify and outline the contours
contours,_ = cv2.findContours(thresh_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contoured_img = img.copy()
cv2.drawContours(contoured_img,contours,-1,yellow,2)
cv2.imshow("draw contour",contoured_img)
cv2.waitKey(0)







