from import picamera, Color 
import os.path as path
import Image 
import time
import psutil

camera = picamera.PiCamera()

count = 0

def img_namer():
  while path.isfile("images/image_" + count + ".jpg")
    count++
    return
    
def take_pic():
  #start the preview
  camera.start_preview();
  #start countdown
  count_down = 5
  camera.annotate_background = Color("White")
  for x in range(0, 5):
    camera.annotate_text = count_down
    count_down--
    time.sleep(1)
  time.sleep(.135)
  #create a shudder effect
  shutter_img = Image.open("shutter_img")
  shutter_img.show();
  camera.capture('image_' + count + ".jpg")
  count++
  time.sleep(.135)
  return
