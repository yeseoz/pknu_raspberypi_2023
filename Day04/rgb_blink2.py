# LED RGB 깜빡이기
import RPi.GPIO as GPIO
import time

red = 17
green = 27
blue = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red,True)
GPIO.output(green,True)
GPIO.output(blue,True) # 여기 까지 초기화

try:
    while True:
        # RED, GREEN = yellow / RED , BLUE = pink / GREEN, BLUE = sky

        GPIO.output(red, False) # RED on
        GPIO.output(green,False)
        GPIO.output(blue,False)
        time.sleep(1)
        GPIO.output(red, True)
        GPIO.output(green,True) #Green on
        GPIO.output(blue,True)
        time.sleep(1)
        # GPIO.output(red, True)
        # GPIO.output(green,True)
        # GPIO.output(blue,False) # Blue on
        # time.sleep(1)


except KeyboardInterrupt : 
    GPIO.cleanup() 