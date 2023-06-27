import RPi.GPIO as GPIO
import time

buzzerPin = 13
melody = [131, 147, 165, 175, 196, 220, 247, 262]
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440)

try:
	while True:
	buzz.start(50)
	for i in range(0, len(melody)):
		buzz.ChangeFrequency(melody[i])
		time.sleep(0.3)
	buzz.stop()
	time.sleep(1)

except KeybordInterrupt: # 키보드 인터럽트
	GPIO.cleanup()
