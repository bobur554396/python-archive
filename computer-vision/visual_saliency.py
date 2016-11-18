import cv2
import numpy as np
from os import path

from saliency import Saliency
from tracking import MultipleObjectsTracker


def main(video_file='soccer.avi', roi=((140, 100), (500, 600))):
    if path.isfile(video_file):
        video = cv2.VideoCapture(video_file)
    elif video_file == 'camera':
        video = cv2.VideoCapture(0)
    else:
        print 'File "' + video_file + '" does not exist.'
        raise SystemExit

    mot = MultipleObjectsTracker()
    while True:
        success, img = video.read()
        if success:
            if roi:
                img = img[roi[0][0]:roi[1][0], roi[0][1]: roi[1][1]]
                #generate saliency map
                sal = Saliency(img, use_numpy_fft=False, gauss_kernel=(3, 3))

        cv2.imshow("tracker", mot.advance_frame(img, sal.get_proto_objects_map(use_otsu=False)))

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break