# USAGE: python CamTest.py

# import the necessary packages
import cv2
import time
import os

# Open Video Camera
vs = cv2.VideoCapture(0)  # 0 is the default camera
yellow = (0,255,255)
time.sleep(2.0)

is_cropping = False
is_resizing = False
is_blurring = False
is_showing_box = False
is_showing_text = False
is_thresholding = False
is_new_function = False 

# loop over the frames from the video stream
while True:
    # grab the frame from video stream
    ret, frame = vs.read()

    original = frame.copy()
    h,w = frame.shape[:2]

    if is_cropping:
        x_start = int(w * 0.2)
        y_start = int(h * 0.2)
        x_end = int(w * 0.8)
        y_end = int(h * 0.8)
        frame = frame[y_start:y_end, x_start:x_end]
    if is_resizing:
        current_h, current_w = frame.shape[:2]
        frame = cv2.resize(frame, (current_w // 2, current_h // 2))
    if is_blurring:
        frame = cv2.GaussianBlur(frame,(25,25),sigmaX=0)
    if is_showing_box:
        frame = cv2.rectangle(frame,(w//4,h//4),(3*w//4,3*h//4),yellow,2)
    if is_showing_text:
        frame = cv2.putText(frame,"Dreams",(100,100),cv2.FONT_HERSHEY_COMPLEX,6,yellow,2)
    if is_thresholding:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 127, 200, cv2.THRESH_BINARY)
        frame = thresh
    if is_new_function:
        # show edge detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
        frame = cv2.Canny(gray_frame,100,200)

    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    
    if key == ord("c") or key == ord("C") :
        is_cropping = not is_cropping
    elif key == ord("r") or key == ord("R"):
        is_resizing = not is_resizing
    elif key == ord("b") or key ==ord("B"):
        is_blurring = not is_blurring
    elif key == ord("a") or key ==ord("A"):
        is_showing_box = not is_showing_box
    elif key == ord("t") or key ==ord("T"):
        is_showing_text = not is_showing_text
    elif key == ord("g") or key ==ord("G"):
        is_thresholding = not is_thresholding
    elif key == ord("n") or key == ord("N"):
        is_new_function = not is_new_function
    elif key == ord("q") or key == ord("Q"):
        break

vs.release()
cv2.destroyAllWindows()
