import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("localhost",1883)
client.loop_start()



while True:

	temperature = random.randrange(20,35)
	print "Temperature : " + str(temperature)
	client.publish("environment/temperature",temperature)
	time.sleep(2)



