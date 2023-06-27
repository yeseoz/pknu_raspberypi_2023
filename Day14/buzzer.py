import RPi.GPIO as GPIO
import time

buzzerPin = 18
melody = [131, 147, 165, 175, 196, 220, 247, 262]
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440) # 440HZ를 갖는 객체 생성

try:
	while True:
		buzz.start(50)
		for i in range(0, len(melody)):
			buzz.ChangeFrequency(melody[i]) # 주파수 변경
			time.sleep(0.3)
			print(i)
		
		buzz.stop()
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
