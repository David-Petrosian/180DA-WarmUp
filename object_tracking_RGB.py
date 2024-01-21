import cv2
import numpy as np

def track_object_rgb():
    cap = cv2.VideoCapture(0)
    lower_rgb = np.array([200, 0, 0])  
    upper_rgb = np.array([255, 100, 200])  
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        color_mask = cv2.inRange(frame, lower_rgb, upper_rgb)
        contours, _ = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('Object Tracking (RGB)', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    track_object_rgb()