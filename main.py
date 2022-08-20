import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
while True: 
 GPIO.output(14, GPIO.HIGH) 
 GPIO.output(15, GPIO.HIGH) 
 sleep(.2)
 GPIO.output(14, GPIO.LOW)
 GPIO.output(15, GPIO.LOW)
 sleep(.2)
