# This app test the motors and creates an up and down

import RPi.GPIO as GPIO
import time
from time import sleep


GPIO.setmode(GPIO.BOARD)
 
GPIO.setwarnings(False)

MotorDIR = 16
MotorPWM = 33

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
 
# Going up
def Go_Up():
    GPIO.output(16,GPIO.HIGH)
    GPIO.output(13,GPIO.HIGH)

 
# Going down
def Go_Down():
    GPIO.output(16,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
 
# stop
def Stop_LA():
    GPIO.output(16,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)

GPIO.cleanup()

setup()
while True:
    Go_Down()
    time.sleep(2)
    Stop_LA()


