import cv2

#default args: sensitivity=800, color=(0, 255, 0), delay =50
gsens = 800
gclr = (0, 255, 0)
gdelay = 50

def main(vids):
    cap = cv2.VideoCapture(vids)
    _, f1 = cap.read()
    _, f2 = cap.read()


    while cap.isOpened():
        diff = cv2.absdiff(f1, f2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < int(gsens):
                continue
            cv2.rectangle(f1, (x, y), ((x+w), (y+h)), gclr, 2)


        cv2.imshow("SimpleSurvo Multi-Track", f1)
        f1 = f2
        _, f2 = cap.read()

        #The delay and exit condition
        if cv2.waitKey(gdelay) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
