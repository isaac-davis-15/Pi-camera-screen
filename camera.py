import picamera 
import os.path as path
import os
from PIL import Image 
import time
from random import randint
import RPi.GPIO as gpio
import datetime as date

camera = picamera.PiCamera()
camera.image_effect = "film"

os.putenv("SDL_FBDEV", "/dev/fb0")

gpio.setmode(gpio.BCM)

count = 0

off_pin = "define me"

todays_date = date.date.today()

def init():
  #set the pin mode of GPIO pins 
  gpio.setup(17, gpio.IN)
  gpio.setup()
return

def check_off():
  if gpio.input(off_pin):
    os.system("sudo shutdown")
return


def take_pic():
  global count  

  #start the preview
  camera.start_preview();
  
  #start countdown
  count_down = 5
  camera.annotate_background = Color("White")
  for x in range(0, 5):
    camera.annotate_text = count_down
    count_down -= 1
    time.sleep(1)
  time.sleep(.135)
  
  #create a shudder effect
  camera.brightness = 100
  camera.stop_preview()
  time.sleep(.5)
  
  #take the photo and some of shutter effect
  camera.capture('./images/' + todays_date + "_" + date. + ".jpg")
  count += 1
  time.sleep(.135)
  camera.brightness = 50
  
  #show the pic that was just taken
  

def slideshow():
  
  return 

init()
current_img = None
while 1 == 1:
  if gpio.input(17):
    take_pic()
  else:
    slideshow()
    time.sleep(5)
    current_img.close()
  check_off()
