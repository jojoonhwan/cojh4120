import paho.mqtt.client as mqtt
import time   # time sleep을 위한 library
import random  # random함수를 쓰기 위한 library

client = mqtt.Client() 
client.connect("localhost",1883) # mqtt 해당 서버에 연결
client.loop_start()



while True: #while(1)과 같음

	temperature = random.randrange(20,35)  #temperature 값을 20~35사이로 랜덤 생성
	print "Temperature : " + str(temperature)
	client.publish("environment/temperature",temperature) # environment/temperature topic의 값에 실행
	time.sleep(2)



