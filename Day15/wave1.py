import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 13
ECHO = 21
buzzerPin = 18
print("초음파 거리측정기")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 550)

GPIO.output(TRIG, False)
print("초음파 출력 초기화")
time.sleep(2)

try:
	while True:
		GPIO.output(TRIG,True)
		time.sleep(0.00001) # 10uS의 펄스 발생을 위한 딜레이
		GPIO.output(TRIG, False)

		while GPIO.input(ECHO)== 0:
			start = time.time() # ECHO핀 상승 시간값 저장
			
		while GPIO.input(ECHO) == 1:
			stop = time.time() # ECHO핀 하강 시간값 저장

		check_time = stop - start
		distance = check_time * 34300 / 2
		print("Distance : %.1f cm" %distance)

		if distance < 15:
			buzz.start(50)
			time.sleep(0.3)
		buzz.stop()
		time.sleep(0.1)

		if distance < 10:
			buzz.start(50)
			time.sleep(0.3) # 0.3간 울리고
		buzz.stop()
		time.sleep(0.07)

		if distance < 5:
			buzz.start(50)
			time.sleep(0.3)
		buzz.stop() #0.5초 텀을 준다
		time.sleep(0.03)

except KeyboardInterrupt:
	print("거리 측정 완료 ")
	GPIO.cleanup()
