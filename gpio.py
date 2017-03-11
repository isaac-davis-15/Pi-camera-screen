import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

gpio.setup(27, gpio.IN)

pin = gpio.input(27)

print pin
