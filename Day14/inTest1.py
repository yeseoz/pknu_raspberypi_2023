import RPi.GPIO as GPIO
import time

swPin = 6
ledPin = 7
flag = True
GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

def my_callback(channel):
	global flag
	if flag == False:
		flag = True
		print(flag)
	else:
		flag = False
		print(flag)

GPIO.add_event_detect(swPin, GPIO.RISING, callback = my_callback)

try:
	while True:
		if flag == True:
			GPIO.output(ledPin, GPIO.HIGH)
		else:
			GPIO.output(ledPin, GPIO.LOW)
except KeyboardInterrupt:
	GPIO.cleanup()
