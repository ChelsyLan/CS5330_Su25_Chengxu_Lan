### WebCam

url : https://www.youtube.com/watch?v=YxJW2yt7zSU

Use while loop to display video frame by frame, use boolean value to keep track of each key,
so that once we press the key, the boolean value can be updated and modify the frame correspondingly

1. crop: cut the frame

2. resize: `cv2.resize()`

3. blur: `cv2.GaussianBlur()`, (25,25) defines we blur the video to what extent

4. add a box: `cv2.rectangle()` define the location,thickness,size of the box

5. add text: `cv2.putText()` defines the content, font, size of the text

6. thresholding: convert the frame to grayscale first, then use `cv2.threshold()` to reset pixel value

7. new function: add edge on the video using `cv2.Canny()`