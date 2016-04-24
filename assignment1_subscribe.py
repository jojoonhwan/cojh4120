import paho.mqtt.client as mqtt

def on_connect(clinet,userdata, flags, rc):

	client.subscribe("environment/temperature")
	client.subscribe("environment/humidity")

def on_message(client,userdata, message):

	global temp, humi, temp1, humi1

	if message.topic == "environment/temperature":

		temp = float(message.payload)
		temp1 = True

	elif message.topic == "environment/humidity":

		humi = float(message.payload)
		humi1 = True

	if temp1 and humi1:

		result = ((9.0/5.0)*temp) - (0.55 *(1.0 - humi) * (((9.0/5.0)*temp) - 26.0)) + 32.0 

		print "Temperature : " +str(temp)
		print "Humidity : " +str(humi)
		print "DIscomport index: " +str(result),

		if result >= 80 :
			print "(very high)\n"
		elif (75<=result) and (result <85):
			print "(high)\n"
		elif (65<=result) and (result<75):
			print" normal\n"
		else :
		 	print"(low)\n"

		 temp1 = False
		 humi1 = False


temp = 0
humi = 0

temp1 = False
humi1 = False

client = mqtt.Client("subscribe_Client")
client.on_connect = on_connect
client.on_message = on_message

client.connet("localhost" , 1883, 60)

client.loop_forever()


