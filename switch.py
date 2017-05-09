import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)

GPIO. setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
url='https://hypothalamic-jackbo.000webhostapp.com/try.php'
val=0

while True:
	input_state = GPIO.input(18)
	if input_state == False:
		print('Button Pressed')
		if val !=0:
			val=0
			payload={'value': 0}
			r=requests.post(url,data=payload)
		time.sleep(0.2)
	else:
		print('Button unpressed')
		if val !=1:
			val=1
			payload={'value': 1}
			r=requests.post(url,data=payload)
		time.sleep(0.2)
