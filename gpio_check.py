import RPi.GPIO as gpio
import os
import time

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN, pull_up_down = gpio.PUD_UP)

def trigger(channel):
	os.system("sudo service display stop")
	os.system("sudo python /home/pi/Pi-camera-screen/take_pic.py")

gpio.add_event_detect(17, gpio.FALLING, callback = trigger, bouncetime = 2000)

while 1:
	time.sleep(1)



 
	
