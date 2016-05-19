import RPi.GPIO as gpio
import time
led_pin = 5
gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)
	
def blinkLED(numTimes, speed):
