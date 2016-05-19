import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
import dht11
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.cleanup()

instance = dht11.DHT11(pin = 5)

temp = 0

mqttc = mqtt.Client("")
mqttc.connect("localhost",1883)

try : 
	while True:
		result = instance.read()
		if result.is_valid():
			temp = result.temperature
			print"Temp : " ,temp,"C"
			mqttc.publish("environment/temperature",temp)
		time.sleep(1)

except KeyboardInterrupt:
	gpio.cleanup()
