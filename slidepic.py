import os 
import os.path
import picamera
import time
import datetime
import RPi.GPIO as gpio
import subprocess 
import signal

#init the camera
camera = picamera.PiCamera()

#set up the GPIO
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN, pull_up_down = gpio.PUD_UP)
#set up time
now = datetime.datetime.now()
str(now)
slides = None
image_name = None

def fileCount(dir):
    count = 0
    for f in os.listdir(dir):
	if os.path.isfile(os.path.join(dir, f)):
	    count += 1
    return count
image_name = fileCount("/home/pi/Pi-camera-screen/images")
image_name += 1

print(image_name)

def slideshow():
    global slides    

    slides = subprocess.Popen("fbi -noverbose -d /dev/fb0 -t 4  /home/pi/Pi-camera-screen/images/*.jpg", shell=True, preexec_fn=os.setsid)

def take_pic(channel):
    global camera
    global slides
    global image_name

    if slides is not None:
    	os.killpg(os.getpgid(slides.pid), signal.SIGTERM)

    camera.start_preview()
    count_down = 5
    for x in range(0, 5):
        camera.annotate_text = str(count_down)
        time.sleep(1)
        count_down -= 1
    time.sleep(.135)

    image_name
    camera.annotate_text = " "
    camera.stop_preview()
    camera.capture("/home/pi/Pi-camera-screen/images/" + str(image_name) + ".jpg") 
    time.sleep(.1)
    taken_image = subprocess.Popen("fbi -noverbose -d /dev/fb0 /home/pi/Pi-camera-screen/images/" + str(image_name) + ".jpg", shell=True, preexec_fn=os.setsid)
    time.sleep(7)
    image_name += 1
    os.killpg(os.getpgid(taken_image.pid), signal.SIGTERM)
    slideshow()

gpio.add_event_detect(17, gpio.FALLING, callback = take_pic, bouncetime = 30000)

slideshow()

while 1:
    time.sleep(.1)
    

	

    
