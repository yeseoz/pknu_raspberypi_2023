# MQTT 패키지 설치 - paho-mqtt
# sudo pip install paho-mqtt
## 동시에 publish(데이터 전송[출판]) / subcribe(데이터 수신[구독]) 처리

from threading import Thread, Timer
import time # time.sleep()
import json # 파이썬에서는 기본 제공 c#에서는 Newthon soft
import datetime as dt

import paho.mqtt.client as mqtt
import Adafruit_DHT as dht

#GPIO
import RPi.GPIO as GPIO

#GPIO, DHT 설정
sensor = dht.DHT11 # 초 저가 센서
rcv_pin = 17
green = 27
servo_pin = 18

# green led init
GPIO.setwarnings(False) # 오류메시지 제거
GPIO.setmode(GPIO.BCM)
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, GPIO.HIGH) # true

#servo init
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 100) # 서보모터 속도, 50~100 주파수
pwm.start(3) # 각도0도 Duty

class publisher(Thread):
    def __init__(self):
        Thread.__init__(self) # Thread 초끼화
        self.host = '210.119.12.55' # 본인pc ip
        self.port = 1883 # 회사에서는 이 포트 그대로 사용하면 안됨
        self.clientId = 'IOT55'
        self.count = 0
        print('publisher 스레드 시작')
        self.client = mqtt.Client(client_id= self.clientId) # 설계대로

    def run(self): # 실행시키는 함수
        self.client.connect(self.host, self.port)

        # self.client.username_pw_set() // id/pw로 로그인할때는 필요
        self.publish_data_auto()

    def publish_data_auto(self):
        humid, temp = dht.read_retry(sensor, rcv_pin)
        curr = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 2023-06-14 10:39:54
        origin_data = {'DEV_ID' : self.clientId,
                        'CURR_DT' : curr,
                        'TYPE' : 'TEMPHUMID',
                        'STAT' : f'{temp} | {humid}'} #sample data
        pub_data = json.dumps(origin_data) # MQTT로 전송할 데이터를 json으로 변환
        self.client.publish(topic='pknu/rpi/control/', payload=pub_data)
        print(f'Data Published # {self.count}')
        self.count = self.count +1
        Timer(2.0, self.publish_data_auto).start() # 2초 마다 출판

# 다른곳 데이터를 받아오는 객체
class subscriber(Thread):
    def __init__(self): # 생성자
        Thread.__init__(self)
        self.host = '210.119.12.55'          
        # self.host = 'https://personar95.azure.com/iotservice'
        # self.host = 'personar95.iot.aws-region.amazonaws.com'
        self.port = 1883
        self.clientId = 'IOT55_SEB'
        self.topic = 'pknu/monitor/control/'    
        print('subscriber 스레드 시작')
        self.client = mqtt.Client(client_id = self.clientId)

    def run(self): # Thread.start() 함수를 샐행하면 실행되는 함수
        self.client.on_connect = self.onConnect # 접속이 성공시그널 처리
        self.client.on_message = self.onMessage # 접속 후 메시지가 수신되면 처리
        self.client.connect(self.host, self.port)
        self.client.subscribe(topic = self.topic)
        self.client.loop_forever()

    def onConnect(self, mqttc, obj, flags, rc):
        print(f'subscriber 연결됨 rc > {rc}')

    def onMessage(self, mqttc, obj, msg):
        rcv_msg = str(msg.payload.decode('utf-8'))
        # print(f'{msg.topic} / {rcv_msg}')
        data = json.loads(rcv_msg) #json data로 형변환
        stat = data['STAT']
        print(f'현재 STAT : {stat}')
        if (stat =='OPEN'):
            GPIO.output(green, GPIO.LOW)
            pwm.ChangeDutyCycle(12) # 90도
        elif(stat =='CLOSE'):
            GPIO.output(green, GPIO.HIGH)
            pwm.ChangeDutyCycle(3) # 90도
        time.sleep(1.0) # 1초

if __name__ =='__main__':
    thPub = publisher() # publisher 객체생성
    thSub = subscriber() # subscriber 객체 생성
    thPub.start() # run() 자동실행
    thSub.start()