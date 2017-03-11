import picamera
import os
import time
import subprocess

camera = picamera.PiCamera()
camera.start_preview()

#camera.annotate_background = red
#rgb(255,255,255)

camera.annotate_text = "Hello"

time.sleep(5)

camera.annotate_text = ""
camera.capture("/home/pi/Pi-camera-screen/images/test_2.jpg")

camera.stop_preview()

subprocess.Popen("./start.sh")

