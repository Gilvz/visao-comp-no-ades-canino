import cv2

class Camera:
    def __init__(self, src=0):
        self.cap = cv2.VideoCapture(src)
    def read(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

def show(self, window_name, frame):
    cv2.imshow(window_name, frame)

def close(self):
    self.cap.release()
    cv2.destroyAllWindows()