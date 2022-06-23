import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

BUTTON_PIN = 26

GPIO.setup(BUTTON_PIN, GPIO.IN)

try:
    while True:
        val = GPIO.input(BUTTON_PIN)
        print(val)

        sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
