import cv2


videoCapture = cv2.VideoCapture('MyInputVid.avi')
fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('MyOutputVid.avi', cv2.cv.CV_FOURCC('I', '4', '2', '0'), fps, size)


clicked = False

def onMouse(event, x, y, flags, params):
    global clicked
    if event == cv2.cv.CV_EVENT_LBUTTONUP:
        clicked = True

# cameraCapture = cv2.VideoCapture(0)
# cv2.namedWindow('MyWindow')
# cv2.setMouseCallback('MyWindow', onMouse)


success, frame = videoCapture.read()

while success and cv2.waitKey(1) == -1 and not clicked: # loop until they're no more frames
    # videoWriter.write(frame)
    # cv2.imshow('MyWindow', frame)
    success, frame = videoCapture.read()

# cv2.destroyWindow('MyWindow')

