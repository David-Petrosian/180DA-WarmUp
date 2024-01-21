import cv2
import numpy as np
from sklearn.cluster import KMeans
def find_dominant_color(image, k=1):
    pixels = image.reshape((image.shape[0] * image.shape[1], 3))
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)
    dominant_color = kmeans.cluster_centers_[0].astype(int)
    return dominant_color
def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        h, w, _ = frame.shape
        rect_x = int(w * 0.3)
        rect_y = int(h * 0.3)
        rect_w = int(w * 0.4)
        rect_h = int(h * 0.4)
        central_rect = frame[rect_y:rect_y+rect_h, rect_x:rect_x+rect_w]
        dominant_color = find_dominant_color(central_rect, k=1)
        cv2.rectangle(frame, (rect_x, rect_y), (rect_x+rect_w, rect_y+rect_h), (0, 255, 0), 2)
        cv2.putText(frame, f'Dominant Color: {dominant_color}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Video Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()