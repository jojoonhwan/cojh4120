import paho.mqtt.client as mqtt
import time  # time sleep 을 위한 library
import random # random 함수를 쓰기 위한 library

client = mqtt.Client()
client.connect("localhost",1883) # mqtt 서버 연결
client.loop_start()



while True: # while(1)과 같음

	humidity  = random.randrange(30,95) #humidity 값을 30~95 사이로 랜덤 발생
	print "humidity : " + str(humidity)
	client.publish("environment/humidity",humidity/100.0) # environment/humidity topic에 실행
	time.sleep(2)



