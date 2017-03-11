import os
import picamera
import time
import datetime
import RPi.GPIO as gpio
import subprocess 

#init the camera
camera = picamera.PiCamera()

#set up the GPIO
gpio.setmode(gpio.BCM)
gpio.setup(27, gpio.IN)
#set up time
now = datetime.datetime.now()
str(now) 

def slideshow():
    while not gpio.input(27):
	subprocess.Popen("fbi -noverbose -d /dev/fb0 -t 4  /home/pi/Pi-camera-screen/images/*.jpg", shell=False)
    
    subprocess.Popen("^C", shell=False)
    take_pic()

def take_pic():
    global camera

    camera.start_preview()
    count_down = 5
    for x in range(0, 5):
        camera.annotate_text = str(count_down)
        time.sleep(1)
        count_down -= 1
    time.sleep(.135)

    curr_loop_time = now
    
    camera.stop_preview()
    camera.capture("/home/pi/Pi-camera-screen/images/" + str(curr_loop_time) + ".jpg")

    subprocess.Popen("fbi -d /dev/fb0 -t 7 /home/pi/Pi-camera-screen/images/" + str(curr_loop_time) + ".jpg", shell=False)
    time.sleep(7)
    subprocess.Popen("^C")
    slideshow()

slideshow()


	

    
