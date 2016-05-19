import paho.mqtt.client as mqtt
import RPi.GPIO as gpio

a = b = c = d = None

LED = (17, 27, 22)

def on_connect(client, userData, flags, rc):
	if rc == 0:
		client.subscribe('environment/temperature')
		client.subscribe('environment/ultrasonic')
		print "OK"
	else:
		print "fail"

def on_message(client, userData, message):
	global a, b, c, d
	if message.topic == 'environment/ultrasonic':
		
		a = float(message.payload)
		b = True
	elif message.topic == 'environment/temperature':
		c = float(message.payload)
		d = True

	if b == True:
		if d == True:
			if c <= 30:
				if a >= 100:
					gpio.output(22, True)
					gpio.output(27, False)
					gpio.output(17, False)
					print"Green"
				elif 30 <= a and a < 100 :
				  	gpio.output(17, False)
					gpio.output(27, True)
					gpio.output(22, False)
					print"Yellow"
				else :
					gpio.output(17, True)
					gpio.output(27, False)
					gpio.output(22, False)
					print"Red"
			else :
				gpio.output(17, False)
				gpio.output(27, False)
				gpio.output(22, False)
				print"off"
			d = False
	 	else:
			
			if c <= 30:
				if a >= 100:
					gpio.output(22, True)
					gpio.output(27, False)
					gpio.output(17, False)
					print"Green"
				elif 30 <= a and a < 100 :
				  	gpio.output(17, False)
					gpio.output(27, True)
					gpio.output(22, False)
					print"Yellow"
				else :
					gpio.output(22, False)
					gpio.output(27, False)
					gpio.output(17, True)
					print"Red"
			else :
				gpio.output(17, False)
				gpio.output(27, False)
				gpio.output(22, False)
				print"off"
		b = False
		print "Distance: ", a, "cm"
		print "Last vaild Temp:", c, " C"



gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
for pin in LED:
	gpio.setup(pin, gpio.OUT)


try:
	client = mqtt.Client("")
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect("localhost", 1883)
	client.loop_forever()
		
except KeyboardInterrupt:
	gpio.cleanup()
