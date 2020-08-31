import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture('vtest.avi')
    _, frame1 = cap.read()
    _, frame2 = cap.read()


    while cap.isOpened():
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 800:
                continue
            cv2.rectangle(frame1, (x, y), ((x+w), (y+h)), (0, 255, 0), 2)


        cv2.imshow("SimpleServo Multi-Track", frame1)
        frame1 = frame2
        _, frame2 = cap.read()

        #The delay and exit condition
        if cv2.waitKey(50) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
