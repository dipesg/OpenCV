# OpenCV

## Day 1

#### Detect Face
![dipesh_face_detected](https://user-images.githubusercontent.com/75604769/153458132-2b4fcd75-df98-4bcb-bc94-fba33dc05f8d.jpg)

**Today I learned how face is detected by using CASCADE CLASSIFIER and detectMultiScale.**
 - I have provided a python file above you can run this file in your system by:
   - ```python detect_faces.py -h``` It will display the way you should approach to get result.
   - Required ```haarcascade_frontalface_default.xml``` is attached in the repo.

## Day 2
![webcam_detection](imges/webcam-detection.gif)

**Today I learned how to detect faces using imutils VideoStream function**
 - Using ```from imutils.video import VideoStream``` and openCV I have successfully detected faces using webcam.
 - use ```python webcam_detection.py -h``` for required way to run the given python file.
 
 
## Day 3
![ezgif-2-c634a2a6ca](https://user-images.githubusercontent.com/75604769/153538157-c31877d5-5aee-4c03-829b-da67f82c7234.gif)

**Today I learned how to detect eye using CASCADE CLASSIFIER.**
 - Using ```haarcascade_eye.xml``` we detect our eye in face.
 - To run above mention python file ```detect_eye.py``` we have to type ```python detect_eye.py -h``` in command prompt by remaining at directory where this file resides  to get a help.
