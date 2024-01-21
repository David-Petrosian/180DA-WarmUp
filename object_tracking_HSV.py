import cv2
import numpy as np

def track_object():
    cap = cv2.VideoCapture(0)
    lower_hsv = np.array([0, 70, 40])
    upper_hsv = np.array([0, 130, 60])

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        color_mask = cv2.inRange(hsv_frame, lower_hsv, upper_hsv)
        contours, _ = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('Object Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    track_object()