'''
simple display of an image in local directory
'''

import cv2
import numpy as np

img = cv2.imread("big-bird.png")
cv2.imshow('my image', img)
cv2.waitKey()
cv2.destroyAllWindows()