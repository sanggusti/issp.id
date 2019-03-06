import cv2

class Camera():
    def __init__(self):
        img = cv2.imread('./images/cry.jpg')
        self.frame = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    def getFrame(self):
        retval, to_return = cv2.imencode('.png',self.frame)
        return to_return