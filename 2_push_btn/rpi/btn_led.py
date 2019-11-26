import RPi.GPIO as GPIO
from time import sleep

# set ip/op vars
led_pin = 7
btn_pin = 8
btn_state = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    # read btn state
    btn_state = GPIO.input(btn_pin)
    if btn_state == GPIO.HIGH
        GPIO.output(led_pin, GPIO.HIGH)
    else if btn_state == GPIO.LOW
        GPIO.output(led_pin, GPIO.LOW)
GPIO.cleanup()