from basecamera import BaseCamera
import cv2

class Camera(BaseCamera):
    @staticmethod
    def frames():
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise RuntimeError('Camera not found')
        while True:
            _, img = cap.read()
            yield cv2.imencode('.jpg',img)[1].tobytes()