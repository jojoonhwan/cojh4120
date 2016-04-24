import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("localhost",1883)
client.loop_start()



while True:

	humidity  = random.randrange(30,95)
	print "humidity : " + str(humidity)
	client.publish("environment/humidity",humidity/100.0)
	time.sleep(2)



