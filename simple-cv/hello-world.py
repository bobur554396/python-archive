from SimpleCV import Camera
import opencv




cam = Camera()

while True:
    img = cam.getImage()
    img.show()
