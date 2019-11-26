import RPi.GPIO as GPIO
from time import sleep

led_pin = 8
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #alternate mode BCM
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(led_pin, GPIO.HIGH)
    sleep(1)
    GPIO.output(led_pin, GPIO.HIGH)
    sleep(1)