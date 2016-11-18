

import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
