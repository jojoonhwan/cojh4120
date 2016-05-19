import paho.mqtt.client as mqtt
import RPi.GPIO as gpio

a = b = c = d = None #on_message에서 사용할 전역 변수 선언

LED = (17, 27, 22) # LED 핀 정의

def on_connect(client, userData, flags, rc): #구독할 TOPIC명 저장
	if rc == 0: 
		client.subscribe('environment/temperature')
		client.subscribe('environment/ultrasonic')
		print "OK" #제대로 동작함을 확인하기 위한 print
	else:
		print "fail"

def on_message(client, userData, message): 
	global a, b, c, d
	if message.topic == 'environment/ultrasonic': # 초음파 센서에서 TOPIC이 전송된 경우
		a = float(message.payload) #값 저장
		b = True
	elif message.topic == 'environment/temperature': #온도 센서에서 TOPIC이 전송된 경우
		c = float(message.payload)
		d = True

	if b == True: #유효한 값일때
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
	 	else: #유효한 값이 아닐때
			
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
for pin in LED: # LED 핀 순차 입력
	gpio.setup(pin, gpio.OUT)


try:
	client = mqtt.Client("")
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect("localhost", 1883)
	client.loop_forever()
		
except KeyboardInterrupt:
	gpio.cleanup()
