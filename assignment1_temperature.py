import paho.mqtt.clinet as mqtt
import time
import random

client = mqtt.Client()
client.connect("localhost",1883)
client.loop_start()



while True:

	temperature = random(20,35)
	print "Temperature : " + str(temperature)
	client.publish("environment/temperature",temprature)
	time.sleep(2)



