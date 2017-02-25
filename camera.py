from import picamera, Color 
import os.path as path
import Image 
import time
import psutil
from random import randint
import RPi.GPIO as GPIO

camera = picamera.PiCamera()

GPIO.setmode(GPIO.BCM)

count = 0

def init():
  #get the number of photos and store it in a var
  while path.isfile("images/image_" + count + ".jpg")
    count++
  #set the pin mode of a GPIO pin  
  gpio.setup(17, GPIO.IN)
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
  camera.capture('images/image_' + count + ".jpg")
  count++
  time.sleep(.135)
  
  #end the prosses handling the image being shown
  for proc in psutil.process_iter():
    if proc.name() == "display":
        proc.kill()
  return

def slideshow():
  rand_num = randint(0, counter)
  current_img = Image.open("image_" + rand_num + ".jpg")
  current_img.show()
  return 

init()
while true:
  if gpio.input(17)
    take_pic()
  else:
    slideshow()
    time.sleep(5)
