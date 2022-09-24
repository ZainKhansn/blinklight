import RPi.GPIO as GPIO
from time import sleep


ledpin = 14
ledpin2 = 15
ledpin3 = 18
ledpin4 = 23
ledpin5 = 24
ledpin6 = 25
ledpin7 = 20
ledpin8 = 21
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledpin,GPIO.OUT)
GPIO.setup(ledpin2,GPIO.OUT)
GPIO.setup(ledpin3,GPIO.OUT)
GPIO.setup(ledpin4,GPIO.OUT)
GPIO.setup(ledpin5,GPIO.OUT)
GPIO.setup(ledpin6,GPIO.OUT)
GPIO.setup(ledpin7,GPIO.OUT)
GPIO.setup(ledpin8,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,1000)
pi_pwm.start(0)
pi_pwm2 = GPIO.PWM(ledpin2,1000)
pi_pwm2.start(0)
pi_pwm3 = GPIO.PWM(ledpin3,1000)
pi_pwm3.start(0)
pi_pwm4 = GPIO.PWM(ledpin4,1000)
pi_pwm4.start(0)
pi_pwm5 = GPIO.PWM(ledpin5,1000)
pi_pwm5.start(0)
pi_pwm6 = GPIO.PWM(ledpin6,1000)
pi_pwm6.start(0)
pi_pwm7 = GPIO.PWM(ledpin7,1000)
pi_pwm7.start(0)
pi_pwm8 = GPIO.PWM(ledpin8,1000)
pi_pwm8.start(0)

while True:
    try:
        for duty in range(0,101,1):
            pi_pwm.ChangeDutyCycle(duty)
            pi_pwm2.ChangeDutyCycle(duty)
            pi_pwm3.ChangeDutyCycle(duty)
            pi_pwm4.ChangeDutyCycle(duty)
            pi_pwm5.ChangeDutyCycle(duty)
            pi_pwm6.ChangeDutyCycle(duty)
            pi_pwm7.ChangeDutyCycle(duty)
            pi_pwm8.ChangeDutyCycle(duty)
            sleep(0.015)
        sleep(0.15)
       
        for duty in range(100,-1,-1):
            pi_pwm.ChangeDutyCycle(duty)
            pi_pwm2.ChangeDutyCycle(duty)
            pi_pwm3.ChangeDutyCycle(duty)
            pi_pwm4.ChangeDutyCycle(duty)
            pi_pwm5.ChangeDutyCycle(duty)
            pi_pwm6.ChangeDutyCycle(duty)
            pi_pwm7.ChangeDutyCycle(duty)
            pi_pwm8.ChangeDutyCycle(duty)
       
            sleep(0.015)
        sleep(0.15)
    except KeyboardInterrupt:
        print("EXIT COMMAND")

        pi_pwm.ChangeDutyCycle(0)
        pi_pwm2.ChangeDutyCycle(0)
        pi_pwm3.ChangeDutyCycle(0)
        pi_pwm4.ChangeDutyCycle(0)
        pi_pwm5.ChangeDutyCycle(0)
        pi_pwm6.ChangeDutyCycle(0)
        pi_pwm7.ChangeDutyCycle(0)
        pi_pwm8.ChangeDutyCycle(0)
        exit()
