import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) 
GPIO.setup(24, GPIO.OUT) 

while True:
  if GPIO.input(23):
     GPIO.output(24, True) 
     time.sleep(10) 
     GPIO.output(24, False)
     time.sleep(5) 
  time.sleep(0.1) 
