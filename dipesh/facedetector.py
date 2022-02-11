import cv2


class FaceDetector:
    def __init__(self, faceCascadePath, eyeCascadePath):
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)
        self.eyecascade = cv2.CascadeClassifier(eyeCascadePath)

    def detect(self, image, scaleFactor=1.1, minNeighbors=5,
               minSize=(30, 30)):
        rects = self.faceCascade.detectMultiScale(image,
                                                  scaleFactor=scaleFactor,
                                                  minNeighbors=minNeighbors,
                                                  minSize=minSize,
                                                  flags=cv2.CASCADE_SCALE_IMAGE)
        return rects
        
    def eyeface_detection(self, gray, frame):
        faces = self.faceCascade.detectMultiScale(gray, 1.3, 5)
        
        for(x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (150, 200, 250), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+h]
            eyes = self.eyecascade.detectMultiScale(roi_gray, 1.1, 3)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (100, 250, 50), 2)
        return frame
        
