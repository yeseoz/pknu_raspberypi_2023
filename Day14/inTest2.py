import RPi.GPIO as GPIO
import time

swPin = 6
ledPin = 7
buzzerPin = 18
flag = True
GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buzzerPin, GPIO.OUT)

melody = [247, 147]
buzz = GPIO.PWM(buzzerPin, 440)

def my_callback(channel):
	global flag
	if flag == False:
		print(flag)
	else:
		flag = False
		print(flag)

GPIO.add_event_detect(swPin, GPIO.RISING, callback = my_callback)

try:
	while True:
		if flag == True:
			GPIO.output(ledPin, GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(ledPin, GPIO.LOW)
			time.sleep(0.1)
			buzz.start(50)
			for i in range(0, len(melody)):
				buzz.ChangeFrequency(melody[i])
				time.sleep(0.1)
		else:
			GPIO.output(ledPin, GPIO.LOW)
			buzz.stop()
except KeyboardInterrupt:
	GPIO.cleanup()
