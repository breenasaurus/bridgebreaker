# This app test the motors and creates an up and down

import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
MotorDIR = 16
MotorPWM = 13
 
GPIO.setup(MotorDIR,GPIO.OUT)
GPIO.setup(MotorPWM,GPIO.OUT)
 
# Going up
define Go_Up():
  GPIO.output(MotorDIR,GPIO.HIGH)
  GPIO.output(MotorPWM,GPIO.LOW)

 
# Going down
define Go_Down():
  GPIO.output(MotorDIR,GPIO.LOW)
  GPIO.output(MotorPWM,GPIO.HIGH)
 
# stop
GPIO.output(MotorDIR,GPIO.LOW)
GPIO.output(MotorPWM,GPIO.LOW)
