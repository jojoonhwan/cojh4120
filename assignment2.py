import RPi.GPIO as gpio
import dht11  
import time
import datetime

trig_pin = 13
echo_pin = 19
LED = (17, 27, 22)
instance = dht11.DHT11(pin=5)

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(trig_pin, gpio.OUT)
gpio.setup(echo_pin, gpio.IN)
for pin in LED: # LED 핀설정
	gpio.setup(pin, gpio.OUT)
result_temp = 0 #초기화

try:
	while True:
		result = instance.read()

		gpio.output(trig_pin, False)
		time.sleep(1)
		gpio.output(trig_pin, True)
		time.sleep(0.00001)
		gpio.output(trig_pin, False)

		while gpio.input(echo_pin) == 0 :
			pulse_start = time.time()
		while gpio.input(echo_pin) == 1 :
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17000
		distance = round(distance,2)

		print"Distance : ", distance, "cm"

		if result.is_valid(): #유효한 온도 입력시
			result_temp = result.temperature #온도값 저장
			print"Temp : %d C" % result_temp
			if result_temp <= 30: #조건에 맞게 LED 설정
				if distance >= 100 :
					gpio.output(22, True)
					gpio.output(27, False)
					gpio.output(17, False)
					print"Green"
				elif distance >= 30 and distance < 100:
				  	gpio.output(22, False)
					gpio.output(27, True)
					gpio.output(17, False)
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
		else: #유효한 값이 아닐 때 LED 설정
			print"Temp : %d C" % result_temp
			if result_temp <= 30:
				if distance >= 100 :
					gpio.output(22, True)
					gpio.output(27, False)
					gpio.output(17, False)
					print"Green"
				elif distance >= 30 and distance < 100:
				  	gpio.output(22, False)
					gpio.output(27, True)
					gpio.output(17, False)
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
		
except KeyboardInterrupt:
	gpio.cleanup()
