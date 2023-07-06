import sys
import RPi.GPIO as GPIO
import time
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

led_pin = 7
buzzer_pin = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)

melody = [131, 147, 165, 175, 196, 220, 247, 262]
buzz = GPIO.PWM(buzzer_pin, 440)

flag = False
bflag = False

class qtApp(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('./button.ui',self)
		self.setWindowTitle('button')

		self.Btn_led.clicked.connect(self.btnledClicked)
		self.Btn_buzzer.clicked.connect(self.btnbuzzerClicked)

	def btnledClicked(self):
		global flag
		if flag == False:
			print(flag)
			GPIO.output(led_pin, GPIO.LOW)
			flag = True
		else:
			print(flag)
			GPIO.output(led_pin, GPIO.HIGH)
			flag = False
	def btnbuzzerClicked(self):
		global bflag
		bflag = True
		if bflag == True:
			try:
				while(bflag):
					print(bflag)
					buzz.start(50)
					for i in range(0, len(melody)):
						buzz.ChangeFrequency(melody[i])
						time.sleep(0.3)
						print(i)
						bflag = False

					buzz.stop()
					time.sleep(1)
			except KeyboardInterrupt:
				GPIO.cleanup()
		else:
			buzz.stop()
		
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = qtApp()
	ex.show()
	sys.exit(app.exec_())

