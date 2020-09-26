import cv2
import time

def main():
    cap = cv2.VideoCapture(0)
    #More Trackers Available
    tracker = cv2.TrackerMOSSE_create()
    succ, img = cap.read()
    #check something about time cam
    time.sleep(1)
    bound_box = cv2.selectROI('Select Object to track and press ENTER', img, False)
    tracker.init(img, bound_box)

    def draw_cont(img, bound_box):
        (x, y, w, h) = int(bound_box[0]), int(bound_box[1]), int(bound_box[2]), int(bound_box[3])
        cv2.rectangle(img, (x, y), ((x+w), (y+h)), (0, 255, 0), 2)
    
    while True:
        succ, img = cap.read()
        succ, bound_box = tracker.update(img)
        if succ:
            draw_cont(img, bound_box)

        cv2.imshow('SimpleSurvo SingleTrack', img)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
