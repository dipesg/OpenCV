from dipesh.facedetector import FaceDetector
import imutils
from imutils.video import VideoStream
import argparse
import cv2

# Setting up Command line argument.
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face",
                help="Path to where the face cascade resides.")
ap.add_argument("-v", "--video",
                help="Path to the (optional) video file.")
args = vars(ap.parse_args())

# Calling our facedetector class
fd = FaceDetector(args["face"])

# Start Webcam
camera = VideoStream(src=0).start()

# Capturing every frame from a videostream.
while True:
    
    # frame manipulation
    frame = camera.read()
    frame = imutils.resize(frame, width=300)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faceRects = fd.detect(gray, scaleFactor = 1.1,
                          minNeighbors = 5, minSize = (30, 30))
    
    frameClone = frame.copy()
    
    # drawing rectangle using four coordinates given by detect function
    for (fX, fY, fW, fH) in faceRects:
        cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
                      (0, 255, 0), 2)
     
     # Displaying detected frame   
    cv2.imshow("Face", frameClone)
    
    # Stop streaming when done by pressing button 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Once q key is pressed all the windows will be closed    
camera.stop()
cv2.destroyAllWindows()
    
