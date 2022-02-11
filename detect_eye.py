from __future__ import print_function
from dipesh.facedetector import FaceDetector
import imutils
from imutils.video import VideoStream
import argparse
import cv2

# Building commandline Parser
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True,
                help="path to where the face cascade resides.")
ap.add_argument("-e", "--eye", required=True,
                help= "Path to where the eye cascade resides.")
args = vars(ap.parse_args())

 # instance Face detector Class
fd = FaceDetector(args["face"], args["eye"])
    
# Start Webcam
camera = VideoStream(src=0).start()


while True:
    # Image processing
    frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Instantiate Eye detection
    eye_cascade = fd.eyeface_detection(gray, frame)

    cv2.imshow("Faces", eye_cascade)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
    
camera.stop()
cv2.destroyAllWindows()