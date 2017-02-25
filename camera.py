from import picamera, Color 
import os.path as path
import Image 
import time

camera = picamera.PiCamera()

count = 0

def img_namer():
  while path.isfile("images/image_" + count + ".jpg")
    count++
    return
    
def take_pic():
  camera.start_preview();
  count_down = 5
  for x in range(0, 5):
    camera.annotate_text = count_down
    count_down--
    time.sleep(1)
  camera.annotate_background = "white"
  camera.capture('image_' + count + ".jpg");
  count++
  return
