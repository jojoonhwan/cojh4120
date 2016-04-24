import paho.mqtt.client as mqtt

def on_connect(clinet,userdata, flags, rc):  # client가 server에서 응답받을 시 callback

	client.subscribe("environment/temperature") # temperature topic을 subscribe하여 읽음
	client.subscribe("environment/humidity")  # humidity topic을 subscribe하여 읽음

def on_message(client,userdata, message):  # server에서 message 받을 시 callback

	global temp, humi, temp1, humi1 # 전역 변수 선언

	if message.topic == "environment/temperature": # topic이 temperature 일 때 출력

		temp = float(message.payload)
		temp1 = True

	elif message.topic == "environment/humidity": # topic이 humidity 일 때 출력

		humi = float(message.payload)
		humi1 = True

	if temp1 and humi1: # temp1 && humi1 연산과 같음

		result = ((9.0/5.0)*temp) - (0.55 *(1.0 - humi) * (((9.0/5.0)*temp) - 26.0)) + 32.0  #불쾌지수

		print "Temperature : " +str(temp)
		print "Humidity : " +str(humi)
		print "DIscomport index: " +str(result),

		if result >= 80 :  #불쾌지수 80이상이면 very high
			print "(very high)\n"
		elif (75<=result) and (result <80): # 75 ~ 80일때 high
			print "(high)\n"
		elif (60<=result) and (result<75): # 60 ~ 75일때 normal
			print" normal\n"
		else :
		 	print"(low)\n" # 60미만 low

		temp1 = False
		humi1 = False

 # 변수 초기화
temp = 0
humi = 0

temp1 = False
humi1 = False

client = mqtt.Client("subscribe_Client")
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost" , 1883, 60)

client.loop_forever()


